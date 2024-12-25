import sys
input= sys.stdin.readline

n = int(input())
a = set(map(int, input().split()))

m = int(input())
a2 = list(map(int, input().split()))

for x in range (m):
    if a2[x] in a :
        print (1, end=' ')
    else :
        print(0, end=' ')