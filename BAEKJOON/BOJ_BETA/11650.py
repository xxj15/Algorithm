import sys 
input = sys.stdin.readline

n = int(input())
result = {}

for i in range (n):
    x, y = map(int, input().split())
    if x not in result:
        result[x]=[]
    result[x].append(y)


for i in sorted(result.keys()):
    for value in sorted(result[i]):
        print(i, value)


