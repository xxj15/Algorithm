# RGB 거리 
import sys
input = sys.stdin.readline

n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]
dp[0] = home[0]

for x in range(1, n):  # x : 집 번호, y : 색깔 ([0]: R, [1]: G, [2]: B)
    dp[x][0] = min(dp[x-1][1], dp[x-1][2]) + home[x][0]  
    dp[x][1] = min(dp[x-1][0], dp[x-1][2]) + home[x][1]  
    dp[x][2] = min(dp[x-1][0], dp[x-1][1]) + home[x][2] 


print(min(dp[n-1]))

