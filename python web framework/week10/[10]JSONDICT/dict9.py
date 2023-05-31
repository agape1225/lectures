
import pickle

obj = {"name": "이순신", "age":56, "check": True}

with open("data.pickle","wb") as f:
    pickle.dump(obj, f)

with open("data.pickle","rb") as f:
    obj2 = pickle.load(f)

print(obj2)

