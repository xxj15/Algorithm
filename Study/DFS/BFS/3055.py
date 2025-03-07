# 탈출 
import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
maps = [list(input().strip()) for _ in range(R)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

water_queue = deque()
queue = deque()

# 물, 고슴도치 위치, 비버 굴 위치 저장
for i in range(R):
    for j in range(C):
        if maps[i][j] == '*':
            water_queue.append((i, j)) # 물의 이동 저장 
        elif maps[i][j] == 'D':
            D = (i, j)
        elif maps[i][j] == 'S':
            queue.append((i, j, 0))  # 고슴도치 이동 저장 - (x, y, 이동 시간)

def bfs():
    visited = [[False] * C for _ in range(R)]

    while queue:
        for _ in range(len(water_queue)): # 물 확산 먼저고려 
            wx, wy = water_queue.popleft()

            for i in range(4):
                next_wx = wx + dx[i]
                next_wy = wy + dy[i]

                if 0 <= next_wx < R and 0 <= next_wy < C: # 제한 범위 설정 
                    if maps[next_wx][next_wy] == '.':  # 빈칸이면 물이 확산
                        maps[next_wx][next_wy] = '*'
                        water_queue.append((next_wx, next_wy))

        for _ in range(len(queue)): # 이후 고슴도치 이동
            x, y, time = queue.popleft()
            
            if (x, y) == D:
                return time

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < R and 0 <= ny < C:
                    # 이동 가능 조건: '.' 또는 'D'이고, 방문하지 않았어야 함
                    if (maps[nx][ny] == '.' or maps[nx][ny] == 'D') and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, time + 1))

    return "KAKTUS"  

print(bfs())