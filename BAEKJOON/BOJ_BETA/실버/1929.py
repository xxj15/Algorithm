# 소수 구하기 
import sys 
input = sys.stdin.readline

n, m = map (int,input().split())

for num in range(n, m+1):
    if num == 1: 
        continue

    is_prime = True
    for j in range (2, int(num**0.5)+1):
        if  num % j == 0 : 
            is_prime=False
            break

    if is_prime == True:
        print(num)