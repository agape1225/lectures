import os
import openai

#api_key = os.environ["api_key"]
openai.api_key = ""


while True :
    prompt = input()
    if prompt == "." : break
    print("Me : " + prompt)    

    messages = []
    messages.append({"role": "user", "content": prompt})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  messages=messages)

    print(completion)
    res= completion.choices[0].message['content']
    
    print("GPT : " +res)