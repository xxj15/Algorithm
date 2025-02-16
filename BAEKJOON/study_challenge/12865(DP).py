# 평범한 배낭 
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

def knapsack(n,k, items):
    dp = [[0] * (K + 1) for _ in range(n + 1)] 

    for i in range(1, n + 1):  
        w, v = items[i - 1] 
        for j in range(k + 1):  
            if j < w:  
                dp[i][j] = dp[i - 1][j]
            else: 
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

    return dp[n][k]  

print(knapsack(N, K, items))
