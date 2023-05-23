import os
import openai

api_key = os.environ["api_key"]
openai.api_key = api_key 

messages = []
    
while True :
    prompt = input()
    if prompt == "." : break
    print("Me : " + prompt)    

    messages.append({"role": "user", "content": prompt})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  messages=messages)

    res= completion.choices[0].message['content']
    messages.append({"role": 'assistant', "content": res}  )

    print("GPT : " +res)