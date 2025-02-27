# 가운데를 말해요
import sys, heapq
input = sys.stdin.readline

N = int(input())

max_heap = []  # 중앙값 이하 값들 저장
min_heap = []  # 중앙값 이상 값들 저장

for i in range(N):
    num = int(input())
    
    if not max_heap or num <= -max_heap[0]:
        heapq.heappush(max_heap, -num)  
    else:
        heapq.heappush(min_heap, num)
    
    # 힙 크기 조정 
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    
    print(-max_heap[0]) # 최대 힙은 음수로 저장했으니까
