import sys
input = sys.stdin.readline
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque(range(1, n + 1))
res = []

# queue에서 k번째 사람을 계속 제거
while queue:
    queue.rotate(-(k - 1))  # k-1번 회전
    res.append(queue.popleft())  # k번째 사람 제거

# 결과 출력
print("<" + ", ".join(map(str, res)) + ">")
