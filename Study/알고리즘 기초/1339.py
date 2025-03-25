#단어 수학
import sys
input = sys.stdin.readline

N = int(input()) # 단어 개수 입력받기 
words=[input().strip() for _ in range(N)] 

weight = {} # 가중치 저장 

# 가중치 포함해서 저장 
for word in words:
    length = len(word)
    for i in range(length):
        char = word[i]

        if char not in weight:
            weight[char] = 10**(length - i-1)

        else: 
            weight[char] += 10**(length - i-1)

sorted_weights = sorted(weight.items(), key=lambda x: x[1], reverse=True)     

ans = 0
num = 9 

for key, value in sorted_weights:
    ans += value * num
    num -= 1

print(ans)