#토마토
import sys 
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()

# 배열 순회하며 1 찾아서 queue에 넣음 
for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 1:
                queue.append((z, x, y))

def bfs():
    days = -1  
    
    while queue:
        days += 1  
        
        for _ in range(len(queue)): 
            z, x, y = queue.popleft()

            for i in range(6):
                nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
                
                if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and tomato[nz][nx][ny] == 0:
                    tomato[nz][nx][ny] = 1 
                    queue.append((nz, nx, ny))

    return days

result = bfs()

# 배열 순회하며 0이 남아있는지 확인 
for z in range(h):
    for x in range(n):
        if 0 in tomato[z][x]: 
            print(-1)
            exit(0)

print(result)
