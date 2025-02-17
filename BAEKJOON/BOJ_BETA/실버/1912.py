# 연속합 
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
sum = [0]*(n)
sum[0] = arr[0]

for i in range(1,n):
    sum[i]= max(arr[i], sum[i-1]+arr[i])

print(max(sum))