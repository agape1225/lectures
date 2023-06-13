from flask import Flask, render_template, request
import openai
import re

openai.api_key = "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"

app = Flask(__name__)

def gpt(song_size):
    print(song_size)

    prompt = f"""
    한국노래 {song_size}개를 추천해주는데 번호. 형식은 "번호. (한국제목(영어제목)) - (한국 가수이름 (영어 가수이름)) '줄바꿈'"으로 해주고 줄바꿈은 \n으로

    위의 리턴값에서 인사말은 빼주고 노래에 대한 정보만 리스트로 리턴해줘"""
   
    messages = []

    messages.append({"role": "user", "content": prompt})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  messages=messages)

    res= completion.choices[0].message['content']
    print(res)

    #return "1. 너도 나처럼 (You like me too) - 수지(Suzy)\n2. 들리나요... (Can you hear me...) - 벤(Ben)\n3. 새벽 가로수길 (Midnight Street) - 노을(Noel)\n4. 이 밤 (This Night) - 진호(Jinho)\n5. 서쪽하늘 (Western Sky) - 양다일(Yang Da Il)"
    return res


@app.route('/')
def tmp_main():
    return render_template("input.html")

@app.route('/input')
def input():
    
    song_size = request.args.get("song_size", 5)
    lines = gpt(song_size).split("\n")

    song_list = []
    for line in lines:
        if line:
            parts = line.split(" - ")
            index = parts[0].split(".")[0].strip()
            title = parts[0].split(".")[1].strip()
            artist = parts[1].strip()
            song_list.append(({'title': index + ". " + title, 'artist': artist}))
    
    print(song_list)
    return render_template("result.html", song_list=song_list)


if __name__ == '__main__':
      app.run(port=8080, debug=True)