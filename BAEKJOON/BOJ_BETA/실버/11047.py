# 동전 0 
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = [int(input().strip()) for _ in range(N)]
coins.reverse()

ans = 0 

for coin in coins:
    if K == 0:
        break
    
    ans += K // coin  
    K %= coin

print(ans)


