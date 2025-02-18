# 동전1
import sys 
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input().strip()) for _ in range(n)]

dp = [0]*(k+1)
dp[0]= 1 # 초기값 설정 - 0원 만드는 방법은 무조건 하나 

for coin in coins:
    for i in range (coin, k+1): 
        dp[i] = dp[i] + dp[ i-coin ]

print(dp[k])

