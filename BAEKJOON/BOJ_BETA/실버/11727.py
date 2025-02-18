# 2xn 타일링 2 
import sys
input = sys.stdin.readline

n = int(input())

ans = [0] * 1001
ans[1] = 1
ans[2] = 3

def dp(i):
    if ans[i]:  
        return ans[i]
    
    for j in range(3, i + 1): 
        ans[j] = (ans[j - 1] + 2 * ans[j - 2]) % 10007 
    return ans[i]

print(dp(n))
