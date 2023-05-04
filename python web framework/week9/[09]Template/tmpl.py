from flask import Flask, render_template

app = Flask(__name__)

@app.route('/tmpl')
def tmpl():    
    return render_template("tmpl.html")

@app.route('/tmpl0')
def tmpl0():    
    return render_template("tmpl0.html")


@app.route('/tmpl1')
def tmpl1():    
    return render_template("tmpl1.html")


@app.route('/tmpl2')
def tmpl2():    
    return render_template("tmpl2.html", msg="Hello World")


@app.route('/tmpl3')
def tmpl3():    
    return render_template("tmpl3.html", lst=["ckt", 53], tpl=('ckt', 53), obj={"name":"ckt", "age":53})


@app.route('/tmpl4')
def tmpl4():    

    objs = [{"name":"홍길동", "age":40},
            {"name":"이순신", "age":50},
            {"name":"임꺽정", "age":60}
            ]

    return render_template("tmpl4.html", objs = objs)

@app.route('/escape')
def escape():    
    return render_template("escape.html", title="<h1>Hello</h1>")

@app.route("/iftest")
def iftest():
    username ="이순신"
    return render_template("iftest.html", username=username, score=87)


@app.route('/loop/')
def loop():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template("loop.html", comments=comments)

@app.route('/loopif/')
def loopif():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template("loopif.html", comments=comments)


@app.route('/loopobjs/')
def loopobjs():

    users = [
        {"name":"이순신", "userid": "lee", "address":"서울시"},
        {"name":"홍길동", "userid": "hong", "address":"인천"},
        {"name":"김유신", "userid": "kim", "address":"제주도"}
    ]

    return render_template("loopobjs.html", users=users)


@app.route('/include')
def include():    
    return render_template("include.html", title="hello")


@app.route('/score')
def score():
    data = [ ["이순신", 90, 80, "" ], ["홍길동", 92, 89, "" ], ["김철수", 70, 65, "" ] ]
    mx = 0
    for d in data :
        sm = d[1] + d[2]
        if sm > mx : mx = sm
    
    for d in data:
        sm = d[1] + d[2]
        if sm == mx :
            d[3] = "👏🏻"

    return render_template("score.html", data=data)




if __name__ == '__main__':
      app.run(port=8080, debug=True)