# 보석 도둑 
import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())

jewels = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]  

jewels.sort()
bags.sort()

max_heap = []
max_value = 0
j = 0

for bag in bags: # 가방을 하나씩 확인하면서 보석을 넣는데, 현재 가방에 담을 수 있는 보석들을 힙에 추가함
    while j < N and jewels[j][0] <= bag:
        heapq.heappush(max_heap, -jewels[j][1])  
        j += 1
    if max_heap:
        max_value += -heapq.heappop(max_heap)

print(max_value)
