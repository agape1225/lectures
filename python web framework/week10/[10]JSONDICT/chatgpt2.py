import requests

api_key = "sk-"

while True :
    prompt = input()
    if prompt == "." : break
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"model": "text-davinci-003", "prompt": prompt,"max_tokens": 200 }


    response = requests.post(
        "https://api.openai.com/v1/completions",
        headers=headers,  json=data,
    )

    res = response.json()["choices"][0]["text"]
    print("User :" + prompt)
    print("GPT :" + res)