# DFS와 BFS 
import sys
input = sys.stdin.readline
from collections import deque  

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]  

# 무방향 그래프 간선 정보 저장 
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True  

visited1 = [False] * (N + 1)  # DFS 방문 여부
visited2 = [False] * (N + 1)  # BFS 방문 여부

# DFS
def dfs(v):
    print(v, end=' ')  # 현재 정점 출력
    visited1[v] = True  # 방문 처리

    # 1번 정점부터 N번 정점까지 탐색
    for i in range(1, N + 1):  
        if graph[v][i] and not visited1[i]:  # 연결되어 있고 방문하지 않았다면 재귀 호출
            dfs(i)

# BFS
def bfs(v):
    queue = deque([v])  # 큐에 시작 정점 삽입
    visited2[v] = True  # 방문 처리

    while queue:  # 큐가 빌 때까지 반복
        node = queue.popleft()  # 큐에서 정점 꺼내기
        print(node, end=' ')  # 현재 정점 출력

        # 1번 정점부터 N번 정점까지 탐색
        for i in range(1, N + 1):  
            if graph[node][i] and not visited2[i]:  # 연결되어 있고 방문하지 않았다면
                queue.append(i)  # 큐에 삽입
                visited2[i] = True  # 방문 처리


dfs(V)  
print()  
bfs(V) 
