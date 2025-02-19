# 포도주 시식 - 틀린 답 
import sys
input = sys.stdin.readline

n = int(input())
drinks = [int(input().strip()) for _ in range(n)]

sorted_drinks = sorted([(drinks[i], i) for i in range(n)], reverse=True)

selected = set()  
total = 0 

for value, idx in sorted_drinks:
    if (idx - 1 in selected and idx - 2 in selected) or (idx + 1 in selected and idx + 2 in selected) or (idx - 1 in selected and idx + 1 in selected):
        continue  

    selected.add(idx)
    total += value

print(total)

