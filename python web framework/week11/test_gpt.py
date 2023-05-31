import re

chat_str = "당신은 백준 알고리즘에서 3일간의 공부 계획을 짜줄 것을 요청하셨습니다. 하루에 3문제씩 C++로 풀 예정이며, 아래는 문제 링크입니다. Day 1: 1. https://www.acmicpc.net/problem/1000 2. https://www.acmicpc.net/problem/10869 3. https://www.acmicpc.net/problem/11720 Day 2: 1. https://www.acmicpc.net/problem/2292 2. https://www.acmicpc.net/problem/2442 3. https://www.acmicpc.net/problem/2753 Day 3: 1. https://www.acmicpc.net/problem/4344 2. https://www.acmicpc.net/problem/4673 3. https://www.acmicpc.net/problem/11653 위의 문제 링크는 모두 백준 알고리즘의 문제이며, C++로 작성된 소스 코드를 제출해야 합니다. 3일간 꾸준한 학습을 통해 알고리즘 실력을 높이기를 바랍니다. 충분히 노력하면 좋은 결과를 얻을 수 있을 것입니다."

str_list = chat_str.split('Day ')

ans_list = []

str_list.pop(0)

day = 3

pattern = r"https://www.acmicpc.net/problem/\d+"
links = re.findall(pattern, chat_str)

# 추출된 링크 출력
for link in links:
    print(link)

    
        
        

    
    
