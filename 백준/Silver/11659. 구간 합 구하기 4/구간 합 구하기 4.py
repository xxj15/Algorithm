import sys
input = sys.stdin.readline

idxNo, outputNo = map(int, input().split())
idx = list (map(int,input().split()))

sumArray = [0]
sum = 0
result = 0

for i in idx:
    sum = sum + i 
    sumArray.append(sum)

for x in range(outputNo):
    a, b = map(int, input().split())
    result = sumArray[b] - sumArray[a-1]
    print(result)