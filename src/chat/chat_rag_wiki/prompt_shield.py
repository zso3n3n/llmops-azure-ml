
from promptflow.core import tool
import requests
import os


@tool
def prompt_shield(prompt: str, context: str):
    # Send a request to the URL
    url = f"{os.environ.get('CONTENT_SAFE_BASE')}contentsafety/text:shieldPrompt?api-version=2024-02-15-preview"
    try:
        headers = {
                "Ocp-Apim-Subscription-Key": os.environ.get("CONTENT_SAFE_KEY"),
                "Content-Type": "application/json",
                }
        
        body = {
                "userPrompt": prompt,
                "documents": [context]
                }
        
        response = requests.post(url=url, headers=headers, json=body)
        promptAttackDetected = response.json()["userPromptAnalysis"]['attackDetected']
        print(promptAttackDetected)

        return promptAttackDetected
    
    except Exception as e:
        print("Get url failed with error: {}".format(e))
        return
    

if __name__ == "__main__":
    prompt_shield("What is the capital of France?", "Paris")
