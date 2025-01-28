# 약수 
import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))

max_num = max(num)
min_num = min(num)

print(max_num*min_num)