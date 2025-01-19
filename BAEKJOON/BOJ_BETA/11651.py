import sys 
input = sys.stdin.readline

n = int(input())
result = {}

for i in range (n):
    x, y = map(int, input().split())
    if y not in result:
        result[y]=[]
    result[y].append(x)


for i in sorted(result.keys()):
    for value in sorted(result[i]):
        print(value, i)

