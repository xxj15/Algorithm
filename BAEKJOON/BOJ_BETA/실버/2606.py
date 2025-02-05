# 바이러스 
import sys
input = sys.stdin.readline

# union-find (경로압축)
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x] 

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

n = int(input())  # 컴퓨터 수
m = int(input())  # 연결된 쌍의 수

parent = list(range(n + 1)) # 각 노드가 자기 자신 가리킴 (부모로)
rank = [0] * (n + 1) # 트리 높이 정보

for _ in range(m):
    a, b = map(int, input().split())
    union(parent, rank, a, b)

root_1 = find(parent, 1) # 1번 컴퓨터가 속한 집합의 루트 노드 반환
connected_num = [i for i in range(1, n + 1) if find(parent, i) == root_1]
ans = len(connected_num) - 1  # 자기 자신 제외

print(ans)
