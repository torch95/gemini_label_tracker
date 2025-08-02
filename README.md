# Gemini API Tracker

This project demonstrates how to use the Google Gemini API with the `google-genai` SDK and Vertex AI backend for tracking API calls with billing labels.

## Configuration

The project uses Google Cloud project authentication with the following configuration:

### Environment Variables
Create a `.env` file in the project root with:
```
GCP_PROJECT_ID=mml-general
GCP_LOCATION=us-central1
```

### Google Cloud Setup
1. **Enable Vertex AI API** in your Google Cloud project
2. **Set up authentication** using one of these methods:
   - Service account key file
   - Application Default Credentials (ADC)
   - gcloud CLI authentication

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up Google Cloud authentication**:
   ```bash
   # Option 1: Using gcloud CLI
   gcloud auth application-default login
   
   # Option 2: Using service account key
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
   ```

3. **Create .env file** (already done with default values):
   ```bash
   # The .env file should contain:
   GCP_PROJECT_ID=mml-general
   GCP_LOCATION=us-central1
   ```

## Usage

Run the main script:
```bash
python main.py
```

The script will simulate API calls for different tenants and track usage with billing labels in Google Cloud.

## Using Labels for Billing Tracking

Labels are used to break down billed charges and track usage per tenant, environment, or any other criteria. Here's how to use them:

### Basic Label Usage

```python
from google import genai

# Initialize client
client = genai.Client(
    vertexai=True,
    project="your-project-id",
    location="us-central1"
)

# Create config with labels
config = {
    "temperature": 0,
    "labels": {
        "tenant_id": "tenant_a",
        "environment": "production"
    }
}

# Make API call with labels
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=["Your prompt here"],
    config=config
)
```

### Label Requirements

- **Format**: Dictionary of string key-value pairs
- **Keys**: Must be lowercase, alphanumeric, with underscores or hyphens
- **Values**: String values only
- **Purpose**: Used to break down billed charges in Google Cloud billing

### Example Label Configurations

```python
# Single tenant label
labels = {"tenant_id": "tenant_a"}

# Multiple labels for detailed tracking
labels = {
    "tenant_id": "tenant_b",
    "environment": "production",
    "service": "chatbot",
    "version": "v1.0"
}

# No labels (for testing)
labels = None
```

### Testing Labels

Run the test script to see labels in action:
```bash
python test_labels.py
```

## Configuration

You can modify the following in `main.py`:
- `PROJECT_ID`: Your Google Cloud project ID (default: "mml-general")
- `LOCATION`: Vertex AI region (default: "us-central1")
- `MODEL_NAME`: The Gemini model to use (default: "gemini-2.5-flash")
- `users_to_simulate`: Dictionary of tenant IDs and call counts

## Billing and Labels

- API calls include billing labels (`tenant_id`) for cost allocation
- Billing data is sent to Google Cloud and can be analyzed in BigQuery
- Labels help track usage per tenant for billing purposes
- Labels are passed through the `config` parameter in `generate_content`

## Notes

- Make sure your Google Cloud project has the Vertex AI API enabled
- Ensure you have proper authentication set up for Google Cloud
- The .env file contains the default project configuration
- Billing labels are automatically added to track usage per tenant
- Labels are used to categorize and track costs in Google Cloud billing # gemini_label_tracker
