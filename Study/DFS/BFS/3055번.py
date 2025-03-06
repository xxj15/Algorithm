# 탈출 
import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())

mapp = [list(map(str, input().strip().split()))for _ in range (C)]
print(mapp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
