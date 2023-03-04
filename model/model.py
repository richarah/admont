import os
import requests
from dotenv import load_dotenv

load_dotenv()

hf_api_key = os.environ["HF_API_KEY"]
hf_model_id = os.environ["HF_MODEL_ID"]

def query(inputs, api_token=os.environ["HF_API_KEY"], model_id=os.environ["HF_MODEL_ID"]):
    payload = {"inputs": inputs, "parameters": {
        "max_length": 10,
        "temperature": 0.1,
        "num_return_sequences": 1,
        }
    }
    headers = {"Authorization": f"Bearer {api_token}"}
    api_url = f"https://api-inference.huggingface.co/models/{model_id}"
    response = requests.post(api_url, headers=headers, json=payload)
    
    # Get just the text
    return response.json()[0]['generated_text']

# data = query("Hello, my dog is cute", hf_api_key, hf_model_id)
# print(data)

# DEBUG
if __name__ == "__main__":
    inp = input("Input: ")
    data = query(inp, hf_api_key, hf_model_id)
    print(data)
