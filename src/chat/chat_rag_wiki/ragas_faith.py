
import os
from promptflow.core import tool
from datasets import Dataset 
from ragas.metrics import faithfulness
from ragas import evaluate
from langchain_openai.chat_models import AzureChatOpenAI
from dotenv import load_dotenv, find_dotenv

@tool
def ragas_faithfulness(prompt: str, context: str, response: str):
    
    data_samples = {
    'question': [prompt],
    'answer': [response],
    'contexts' : [context.split(".")],
    }
    dataset = Dataset.from_dict(data_samples)
    
    azure_model = AzureChatOpenAI(
        openai_api_version="2023-05-15",
        azure_endpoint=os.environ.get('AZURE_OPENAI_ENDPOINT'),
        azure_deployment=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME'),
        model="gpt-4",
        validate_base_url=False,
    )

    score = evaluate(dataset, llm=azure_model, metrics=[faithfulness])

    return score
    

if __name__ == "__main__":
    load_dotenv(find_dotenv(), override=True)
    score = ragas_faithfulness(
                prompt = "Who was the second president of the United States?",
                context = "John Adams was the second president. John Adams was the Uncle of John Quincy Adams",
                response = "Ben Franklin was the 2nd president."
                )
    print(score)
