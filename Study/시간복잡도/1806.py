#부분합 
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
total = 0
min_len = float('inf') 

while True:
    if total >= S:
        min_len = min(min_len, right - left)
        total -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        total += arr[right]
        right += 1

print(0 if min_len == float('inf') else min_len)
