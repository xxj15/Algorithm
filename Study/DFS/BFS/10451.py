# 순열 사이클 
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    per = list(map(int, input().split())) # 순열 입력 받음 
    
    visited = [False] * (N + 1) 
    cnt = 0 # 사이클 카운트 함 

    for i in range(1, N + 1):
        if not visited[i]: # 방문하지 않은 노드에서 시작 
            cnt += 1 # 단일 사이클이더라도 사이클 생성되는건 맞으니 cnt + 1 해줌 
            cur = i # 현재 i번째 노드임. 
            while not visited[cur]:
                visited[cur] = True
                cur = per[cur - 1]  # 간선 이어줌 

    print(cnt)
