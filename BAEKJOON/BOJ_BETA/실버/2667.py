#단지번호 붙이기 
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
apt = [list(map(int, ''.join(input().split()))) for _ in range(n)]
result = []

# 이동가능 방향 - 위 아래 오른쪽 왼쪽 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0] 

queue = deque()

def bfs(graph, i, j):
    queue.append([i, j])
    apt[i][j]=-1  # 방문처리 
    cnt = 1 

    while queue: 
        x, y = queue.popleft()
        apt[x][y] = -1 

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0<= next_x < n and 0 <= next_y < n and apt[next_x][next_y]==1:
                apt[next_x][next_y]=-1
                queue.append([next_x, next_y])
                cnt += 1
    
    return cnt


# 지도 내 아파트 방문 
for i in range(n):
    for j in range(n):
        if apt[i][j] == 1: 
            cnt = bfs(apt, i, j)
            result.append(cnt)


# 결과값 출력 
result.sort()

print(len(result))
for i in result:
    print(i)