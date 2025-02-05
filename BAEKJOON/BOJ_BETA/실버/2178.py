#미로 탐색 
from collections import deque
import sys 
input = sys.stdin.readline

n, m = map(int,input().split())
maze = [list(map(int, ''.join(input().split()))) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque([(0, 0, 1)]) # 시작 좌표 queue에 넣기 
# cnt = 이동 거리 

visited = list([False]*m for _ in range(n))
visited[0][0]=True

while queue: # queue가 빌때까지 진행  
    x, y, cnt = queue.popleft()
    if x == n-1 and y == m-1 :
        print(cnt)
        break

    for i in range(4): 
        next_x = x + dx[i]
        next_y = y + dy[i] 

        if 0<= next_x < n and 0 <= next_y < m : # 미로 벗어나지 않도록 
            if maze[next_x][next_y] == 1 and visited[next_x][next_y]==False: 
                queue.append((next_x,next_y, cnt+1))
                visited[next_x][next_y]= True



