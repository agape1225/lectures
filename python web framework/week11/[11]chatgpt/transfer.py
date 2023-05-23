import os
import openai

api_key = os.environ["api_key"]
openai.api_key = api_key 

txt = "여우가 게으른 개를 뛰어 넘었다"
mode = "영어"

change = {
    "낚시":"다음 문장을 낚시성 스타일로 바꿔주세요 ",
    "영어" : "다음 문장을 영어로 번역해 주세요 ",
}

prompt = change[mode] + "\n" + txt

messages = []

messages.append({"role": "user", "content": prompt})
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  messages=messages)

res= completion.choices[0].message['content']
print("원문 : " +  txt.strip())
print(f"변환({mode}) : " +  res)