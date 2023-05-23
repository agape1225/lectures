import openai
import pandas as pd
import os

api_key = os.environ["api_key"]
openai.api_key = api_key 

file = "data_score.xlsx"
input = "모든 과목의 평균을 알려주세요"

df = pd.read_excel(file)

prompt = f"""
You are working with a pandas dataframe in Python. The name of the dataframe is `df`.
You should use the tools below to answer the question posed of you:
This is the result of `print(df)`:
{df}
Begin!
Question: {input}
"""

print(prompt)

messages = []
messages.append({"role": "user", "content": prompt})
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
res = completion.choices[0].message['content']
print(res)