from jmd_imagescraper.core import *
import os
import zipfile

# 이미지를 다운로드합니다.
duckduckgo_search("", "output3", "face" , max_results=10, img_size= ImgSize.Medium)

# 파일 이름을 변경합니다.
folder = "./output3"
for i, file_name in enumerate(os.listdir(folder)):
    os.rename(os.path.join(folder, file_name), os.path.join(folder, f"face{i+1}.jpg"))


with zipfile.ZipFile("faces.zip", "w") as zipf:
    for file_name in os.listdir(folder):
        zipf.write(os.path.join(folder, file_name))    