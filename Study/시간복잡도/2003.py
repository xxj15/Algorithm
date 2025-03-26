# 수들의 합 2
# 투포인터 - 시간복잡도 O(N)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

ans = 0
left = 0
right = 0
total = 0

while True:
    if total >= M:
        total -= numbers[left]
        left += 1

    elif right == N: # 범위 끝 도착 
        break
    
    else:
        total += numbers[right]
        right += 1

    if total == M:
        ans += 1

print(ans)
