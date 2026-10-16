import requests
from pprint import pprint


headers = {
    "Content-Type": "application/json"
}


data = {
    "model": "llama3.2",
    "messages": [
        {"role": "user", "content": "Hello Ollam, Are you Running?"}
    ]
}


ollama_local_url = "http://localhost:11434"

response = requests.post(url=f"{ollama_local_url}/v1/chat/completions", headers=headers, json=data)

# pprint(response.json())

if response.status_code == 200:
    print("Success! llama3.2 is running")
    print(response.json())
else:
    print(f"Error, status code: {response.status_code}")
    print(f"error detail: {response.text}")
