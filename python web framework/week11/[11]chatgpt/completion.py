import os
import openai
import urllib.request

api_key = os.environ["api_key"]
openai.api_key = api_key


model_engine = "text-davinci-003"

prompt = "chatGPT에 대해서 설명해줘"

completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
print(completion.choices[0].text)