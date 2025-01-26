import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

queue = deque(range(1, n + 1))
res = []

while queue:
    queue.rotate(-(k - 1))  # k-1번 회전
    res.append(queue.popleft())  


print("<" + ", ".join(map(str, res)) + ">")
