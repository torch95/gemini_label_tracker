import os
from dotenv import load_dotenv
from gemini_tracker import GeminiTracker

# Load environment variables from .env file
load_dotenv()

# --- 설정 ---
# 중요: 아래 값을 실제 Google Cloud 프로젝트 정보로 변경하세요.
# 환경 변수에서 값을 가져오거나 직접 입력할 수 있습니다.
PROJECT_ID = os.environ.get("GCP_PROJECT_ID", "mml-general")
LOCATION = os.environ.get("GCP_LOCATION", "us-central1")

# 사용할 Gemini 모델 이름
MODEL_NAME = "gemini-2.5-flash"

def main():
    """
    메인 실행 함수.
    
    GCP 결제 추적을 위한 라벨이 포함된 Gemini API 호출을 시뮬레이션합니다.
    실제 비용 분석은 GCP 콘솔의 BigQuery에서 수행됩니다.
    """
    # 0. 프로젝트 정보가 설정되었는지 확인
    if PROJECT_ID == "YOUR_PROJECT_ID" or LOCATION == "YOUR_LOCATION":
        print("오류: main.py 파일 상단의 PROJECT_ID와 LOCATION을 실제 값으로 설정해주세요.")
        print("또는 GCP_PROJECT_ID, GCP_LOCATION 환경 변수를 지정할 수 있습니다.")
        return

    # 1. GeminiTracker 초기화
    tracker = GeminiTracker(project_id=PROJECT_ID, location=LOCATION, model_name=MODEL_NAME)

    # 2. 여러 사용자가 API를 호출하는 시나리오 시뮬레이션
    print("--- Labeled API Call Simulation Start ---")
    users_to_simulate = {
        "tenant-a": 5,
        "tenant-b": 12,
        "tenant-c": 3,
        "tenant-d": 10,
        "no-label": 5
    }

    for user_id, call_count in users_to_simulate.items():
        print(f"\nSimulating {call_count} calls for '{user_id}'...")
        for i in range(call_count):
            # 실제 API를 호출하여 라벨을 GCP로 전송합니다.
            tracker.track_and_generate(
                user_id=user_id, 
                prompt="This is a test prompt."
            )
            
    print("\n--- Labeled API Call Simulation Complete ---")
    print("\nBilling data with labels has been sent to Google Cloud.")
    print("You can now analyze the cost allocation in BigQuery after a few hours/days.")

if __name__ == "__main__":
    main()