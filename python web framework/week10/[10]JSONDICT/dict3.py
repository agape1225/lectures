datas = { "이순신" : {"age":56, "check": True},
          "홍길동" : {"age":45, "check": False},
          "임꺽정" : {"age":23, "check": True}}

print(datas["홍길동"]["age"])

datas = [
     {"name": "이순신", "age":56, "check": True},
     {"name": "홍길동", "age":45, "check": False},
     {"name": "임꺽정", "age":23, "check": True}
]
print(datas[0]["name"], datas[0]["age"])
