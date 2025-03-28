#내려가기 
import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

inf = float('inf')

dp_max = arr[0][:]
dp_min = arr[0][:]

for i in range(1, N): 
    now_max = [0] * 3
    now_min = [inf] * 3

    for j in range(3): 
        for dx in [-1, 0, 1]: 
            nx = j + dx

            if 0<= nx <3:
                now_max[j] = max(now_max[j], dp_max[nx] + arr[i][j])
                now_min[j] = min(now_min[j], dp_min[nx] + arr[i][j])

    dp_max = now_max
    dp_min = now_min

print(max(dp_max), min(dp_min))

