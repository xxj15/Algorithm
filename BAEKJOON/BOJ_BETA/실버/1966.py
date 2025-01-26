# 프린터 큐 문제 
import sys
from collections import deque
input = sys.stdin.readline 


tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    priorities = deque(map(int, input().split()))  # 중요도를 저장 

    # index랑 priority 같이 저장할 수 있게 함 - enumerate 이용! 
    queue = deque((idx, priority) for idx, priority in enumerate(priorities))

    # enumerate(priorities)는 각 문서의 인덱스와 중요도를 튜플로 반환

    ans = 0

    while queue : 
        cur = queue.popleft() # 가장 왼쪽에 있는 요소 뽑아내기 

        # if any문 사용 - 현재 문서보다 중요도가 더 높은 문서가 있는지 확인!!
        if any(cur[1] < other[1] for other in queue):
            queue.append(cur)
        else:
            ans += 1  # 현재 문서를 인쇄
            if cur[0] == m:  # 목표 문서 인쇄 여부 확인 
                print(ans)
                break

