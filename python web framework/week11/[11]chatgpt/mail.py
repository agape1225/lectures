#set abc=hello
import os
import openai
api_key = os.environ["api_key"]
openai.api_key = api_key 


subject = "오늘 오전에 다툰 사건"
to = "친구"
style = "서운한 감정이 드러나도록" 

prompt = f"""
당신은 글을 매우 잘쓰는 작가입니다. 
아래와 같은 내용으로 {style} 메일을 작성해주세요.
내용 :  {subject}
대상 :  {to}
"""

messages = []
messages.append({"role" :"user", "content": prompt})

completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  messages=messages)

res= completion.choices[0].message['content']
print(res)