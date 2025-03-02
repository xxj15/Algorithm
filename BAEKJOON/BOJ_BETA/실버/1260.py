# DFS와 BFS
import sys

input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)] 

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True  

visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)

def dfs(v):
    print(v, end=' ')
    visited1[v] = True
    for i in range(1, N + 1):  
        if graph[v][i] and not visited1[i]:  # 연결되어 있고 방문하지 않았음.
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited2[v] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in range(1, N + 1):  # 작은 번호부터 방문
            if graph[node][i] and not visited2[i]:
                queue.append(i)
                visited2[i] = True

dfs(V)
print()
bfs(V)
