# 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque() # 수빈 좌표 삽입
max_num = 100000
visited = [-1] * (max_num + 1)

def bfs(): 
    queue.append(n)
    visited[n]=0

    while queue: 
        x = queue.popleft() # 수빈이 위치 
        

        if x == k : # 수빈이와 동생이 만남 
            print(visited[x])
            break

        for i in  (x-1, x+1, x*2): # 다른 방향들 
            if 0<=i<=max_num and visited[i]==-1:
                visited[i] = visited[x] + 1 # 움직인 횟수 추가해주기 
                queue.append(i)


bfs()
