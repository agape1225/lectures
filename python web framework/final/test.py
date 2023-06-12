from flask import Flask, render_template

app = Flask(__name__)

#def gpt():
#     return "1. 너도 나처럼 (You like me too) - 수지(Suzy)\n2. 들리나요... (Can you hear me...) - 벤(Ben)\n3. 새벽 가로수길 (Midnight Street) - 노을(Noel)\n4. 이 밤 (This Night) - 진호(Jinho)\n5. 서쪽하늘 (Western Sky) - 양다일(Yang Da Il)"

@app.route('/')
def index():
    #return render_template("input.html")
    return "hello"


@app.route('/input')
def input():
    #lines = gpt().split("\n")

    #song_list = []
    # for line in lines:
    #     if line:
    #         parts = line.split(" - ")
    #         index = parts[0].split(".")[0].strip()
    #         title = parts[0].split(".")[1].strip()
    #         artist = parts[1].strip()
    #         song_list.append(({'title': index + ". " + title, 'artist': artist}))
    
    #print(song_list)
    return render_template("result.html")


@app.route('/make')
def quiz() :
    subject = request.args.get("subject", "")
    num = int(request.args.get("num", 5))
    prompt  = f"""
    당신은 블러그의 운영자 입니다. {subject} 퀴즈 5개를 4개의 보기로 작성하려고 합니다. 
    please generate  python code to write excel file using dataframe in table format with 7 columns.
    please save the excel file as {subject}.xlsx.
    python 코드만 작성하고 설명이나 주석없이 코드만 알려주세요

    column 1 :  문제, column 2 : 보기1, column 3 :  문제2, column 4 : 보기3,   
    column 5: 보기4, column 6 : 정답, column 7 : 정답설명

    단 to_excel() 메소드를 사용할 때 저장하는 파일의 경로는 바로 C드라이브 밑으로 저장되게 해줘

    """

    print(prompt)
    messages = []
    messages.append({"role": "user", "content": prompt})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    res = completion.choices[0].message['content']
    print(res)
    exec(res)    
    return  "code : <br/>" + res.replace("\n", "<br/>").replace(" "," &nbsp;")