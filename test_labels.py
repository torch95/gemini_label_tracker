#!/usr/bin/env python3
"""
Test script to demonstrate how to use labels with generate_content.
"""

import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

def test_labels():
    """Test how labels work with generate_content."""
    
    # Initialize the client
    client = genai.Client(
        vertexai=True,
        project=os.environ.get("GCP_PROJECT_ID", "mml-general"),
        location=os.environ.get("GCP_LOCATION", "us-central1")
    )
    
    # Test different label configurations
    test_cases = [
        {
            "name": "Basic tenant label",
            "labels": {"tenant_id": "tenant_a"},
            "prompt": "Hello, this is a test."
        },
        {
            "name": "Multiple labels",
            "labels": {
                "tenant_id": "tenant_b",
                "environment": "production",
                "service": "chatbot"
            },
            "prompt": "What is the weather like?"
        },
        {
            "name": "No labels",
            "labels": None,
            "prompt": "Simple test without labels."
        }
    ]
    
    for test_case in test_cases:
        print(f"\n--- Testing: {test_case['name']} ---")
        print(f"Labels: {test_case['labels']}")
        
        try:
            # Create config with labels
            config = {
                "temperature": 0,
                "labels": test_case['labels']
            }
            
            # Make the API call
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[test_case['prompt']],
                config=config
            )
            
            print(f"Response: {response.text[:100]}...")
            print("✅ Success!")
            
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_labels() 