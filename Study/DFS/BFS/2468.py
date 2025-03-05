#안전 영역 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) #dfs 작성하는 경우, 재귀횟수 커지면 제한 풀어줘야 함 

N = int(input())
land = [list(map(int, input().split())) for _ in range(N)]

min_height = min(map(min, land))
max_height = max(map(max, land))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, visited, tmp_land):
    visited[x][y] = True
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and tmp_land[nx][ny] > 0:
            dfs(nx, ny, visited, tmp_land)

ans = 0

for rain in range(0, max_height + 1):
    visited = [[False] * N for _ in range(N)]
    
    tmp_land = [[land[i][j] if land[i][j] > rain else 0 for j in range(N)] for i in range(N)] # land 배열 바로 변경하면 안됨
    
    cnt = 0
    for i in range(N):
        for j in range(N):
            if tmp_land[i][j] > 0 and not visited[i][j]:
                cnt += 1
                dfs(i, j, visited, tmp_land)
    
    ans = max(ans, cnt)

print(ans) 