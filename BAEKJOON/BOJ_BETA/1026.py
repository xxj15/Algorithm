import sys
input= sys.stdin.readline

n = int(input())

list1 = list(map(int, input().strip().split()))
list2 = list(map(int, input().strip().split()))

list1.sort()
list2.sort(reverse=True)

result = 0

for i in range (n):
    result += list1[i]*list2[i]

print(result)