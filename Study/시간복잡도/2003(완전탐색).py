# 수들의 합 2 
# 부분합 이용한 완전탐색 - O(N^2)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

ans = 0

for left in range(N): 
    total = 0 
    for right in range(left, N):
        total += numbers[right]

        if total == M :
            ans += 1 
            break
        elif total > M :
            break

print(ans)