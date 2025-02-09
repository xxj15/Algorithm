#환상의 짝꿍 
from math import isqrt
import sys
input = sys.stdin.readline

MAX_N = int(1.4 * 10**6)
p = [True] * (MAX_N + 1)
p[0] = p[1] = False

for i in range(2, isqrt(MAX_N) + 1):
    if p[i]:
        for j in range(i * i, MAX_N + 1, i):
            p[j] = False

prime = set(i for i in range(2, MAX_N + 1) if p[i])

def is_prime(n):
    if n <= MAX_N:
        return p[n]  
    for i in prime: 
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    s = sum(map(int, input().split()))
    
    if s <= 3:  
        print("NO")
    elif s % 2 == 0: # 두 수의 합이 짝수인 경우 (골드바흐의 추측)
        print("YES")
    else:
        if is_prime(s - 2):
            print("YES")
        else:
            print("NO")
