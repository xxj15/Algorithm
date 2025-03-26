# 수들의 합 2
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
ans = 0
left = 0

for left in range(0,N):
    for right in range(left,N):
        sum = 0
        for i in range(left, right + 1):
            sum += numbers[i]

        if sum == M :
            ans += 1
            break


print(ans)