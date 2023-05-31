import requests

api_key = "sk-"

headers = {"Authorization": f"Bearer {api_key}"}
data = {"model": "text-davinci-003", "prompt": "Chat GPT 설명해주세요..","max_tokens": 200 }

response = requests.post(
     "https://api.openai.com/v1/completions",
     headers=headers,  json=data,
)

res = response.json()["choices"][0]["text"]
print(res)