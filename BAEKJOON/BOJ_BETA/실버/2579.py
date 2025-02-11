# 계단오르기 
import sys
input = sys.stdin.readline

n = int(input())
a = [0]*301 # 인덱스 맞추기 위해 출발지점 가중치 0으로 할당 

for i in range(n):
    a[i+1]= int(input())

dp = [0]* 301 

dp[1] = a[1]
dp[2] = a[1]+a[2]
dp[3] = max(a[1]+a[3], a[2]+a[3])

if n>=4:
    for i in range (4,n+1):
        dp[i] = max(dp[i-2] + a[i], dp[i-3] + a[i-1] + a[i])

print(dp[n])
