# 포도주 시식 - DP 
import sys
input = sys.stdin.readline

n = int(input())
drinks = [int(input().strip()) for _ in range(n)]

dp = [0] * n


if n == 1 : 
    print(drinks[0])
    exit(0)

dp[0] = drinks[0]

if n > 1 : 
    dp[1]= drinks[0] + drinks[1]
    
if n > 2:
    dp[2]= max(drinks[0]+drinks[1], drinks[0]+drinks[2], drinks[1]+drinks[2])


for i in range(3, n):
    dp [i] = max(dp[i-1],  dp[i-2] + drinks[i],  dp[i-3] + drinks[i-1] + drinks[i])

print(dp[n-1])
