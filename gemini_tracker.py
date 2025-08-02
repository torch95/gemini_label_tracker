from google import genai
import os

class GeminiTracker:
    """
    사용자별 Gemini API 호출을 추적하고 실행하는 클래스.
    이 클래스는 라벨링을 지원하는 `google.genai` SDK를 Vertex AI 백엔드와 함께 사용합니다.
    """

    def __init__(self, project_id: str, location: str, model_name: str):
        """
        GeminiTracker를 초기화합니다.

        Args:
            project_id: Google Cloud 프로젝트 ID.
            location: Vertex AI 리전 (예: "us-central1").
            model_name: 사용할 Gemini 모델의 이름.
        """
        # google-genai SDK를 Vertex AI 백엔드와 함께 초기화
        self.client = genai.Client(
            vertexai=True,
            project=project_id,
            location=location)
        # 모델 이름을 저장합니다.
        self.model_name = model_name

    def track_and_generate(self, user_id: str, prompt: str) -> str:
        """
        GCP 결제 추적을 위한 라벨과 함께 Gemini API를 호출합니다.

        Args:
            user_id: API를 호출하는 사용자의 고유 식별자 (테넌트 ID).
            prompt: 모델에 전달할 프롬프트 문자열.

        Returns:
            Gemini 모델이 생성한 텍스트 응답.
        """
        print(f"API call by '{user_id}' with billing label.")

        # GCP 결제 추적을 위해 API 호출에 라벨을 추가합니다.
        # 라벨 키는 소문자, 숫자, 밑줄, 하이픈만 사용할 수 있습니다.
        if user_id == "no-label":
            request_labels = None
        else:
            request_labels = {"tenant_id": user_id.lower().replace("-", "_")}

        # `google.genai` SDK를 Vertex AI 백엔드와 함께 사용할 때,
        # 라벨은 config의 labels 필드를 통해 전달하여 결제 추적을 할 수 있습니다.
        config = {
            "temperature": 0,
            "labels": request_labels
        }

        # client.models에서 generate_content를 호출합니다.
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[prompt],
            config=config
        )
        return response.text 