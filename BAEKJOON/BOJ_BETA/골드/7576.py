import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
for x in range(n):
    for y in range(m):
        if tomato[x][y] == 1:
            queue.append((x, y))

def bfs():
    days = -1  
    while queue:
        days += 1  
        for _ in range(len(queue)): 
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                    tomato[nx][ny] = 1  
                    queue.append((nx, ny))  

    return days

result = bfs()

for row in tomato:
    if 0 in row:
        print(-1) 
        exit(0)

print(result)  
