# 최소 스패닝 트리 
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c)) 

# Kruskal - 가중치 오름차순으로 정렬한 후 추가 
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x]) # 경로 압축 과정 
    return parent[x]


def union(parent, rank, x, y): # 두 집합(루트 노드 root_x와 root_y) 합침
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


def kruskal(v, edges):
    edges.sort(key=lambda x: x[2])  # 가중치 기준 정렬 
    parent = list(range(v + 1)) # 각 노드가 자기 자신 가리킴 (부모로)
    rank = [0] * (v + 1)
    
    mst_weight = 0
    for u, v, weight in edges:
        if find(parent, u) != find(parent, v): # 사이클 발생하지 않으면 MST에 추가 
            union(parent, rank, u, v) # 두 집합 병합
            mst_weight += weight
    
    return mst_weight

print(kruskal(v, edges))

