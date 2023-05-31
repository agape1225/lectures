obj = {"name": "이순신", "age":56, "check": True}
print(obj)

key = "이름"
obj = {key:"이순신"}
print(obj)

#print(obj["age"])   # 예외발생
print(obj.get("age"))
print(obj.get("age", 0))
print( not ( "이름" in obj) )

obj["score"] = 100
obj[key] = "홍길동"
print(obj)    