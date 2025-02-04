#가로수 
import sys, math
input = sys.stdin.readline
from functools import reduce

n = int(input())
tree = [int(input()) for _ in range(n)]
space = [tree[i+1] - tree[i] for i in range(n-1)] 
gcd_value = reduce(math.gcd, space) # 최소공약수를 구할 때 reduce함수와 math.gcd를 이용함

ans = (sum(space) // gcd_value) - len(space)
print(ans)