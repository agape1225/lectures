import pandas as pd
import glob


files = glob.glob("*.xlsx")

df = pd.read_excel(files[0])


for  i, row in df.iterrows():
    print(f"문제 : {row['문제']}") 
    print(f"1. {row['보기1']} ") 
    print(f"2. {row['보기2']} ") 
    print(f"3. {row['보기3']} ") 
    print(f"4. {row['보기4']} ")
    print("--------------------")

