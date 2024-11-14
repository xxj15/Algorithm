import sys
input= sys.stdin.readline

n = int(input())
a = list(int(input()) for _ in range(n))

a.sort()

for x in a:
    print(x)