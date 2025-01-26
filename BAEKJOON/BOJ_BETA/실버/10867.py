import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split())) 
ans = []

for i in nums: 
    if i in ans:
        continue
    else : 
        ans.append(i)

ans.sort()

print(" ".join(map(str, ans)))