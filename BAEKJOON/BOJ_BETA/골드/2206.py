#벽 부수고 이동하기
from collections import deque 
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] # 방문 여부 
queue = deque([(0, 0, 0)]) # (x, y, 벽을 부쉈는지 여부)
visited[0][0][0]=1 #[x좌표][y좌표][벽 부쉈는지 여부]

def bfs():
    while queue:
        x, y, br = queue.popleft()

        if x == n-1 and y == m-1 :
            return visited[x][y][br]
            
        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i] 

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visited[nx][ny][br] == 0: # 벽이 없는 경우 
                    visited[nx][ny][br] = visited[x][y][br] + 1
                    queue.append((nx, ny, br))
                
                elif arr[nx][ny] == 1 and br == 0: # 벽이 있는 경우 (부순 횟수: 0)
                    visited[nx][ny][1] = visited[x][y][br] + 1
                    queue.append((nx, ny, 1))
    
    return -1

print(bfs())



