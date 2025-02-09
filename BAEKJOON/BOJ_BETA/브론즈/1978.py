# 소수 찾기 
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ans = 0
list=[]

for num in nums:
    if num == 1: # i =  1
        continue

     
    is_prime = True
    for j in range (2, int(num**0.5)+1): # i가 2로 나누어지거나 (짝수), 다른 수로 나누어떨어짐 (홀수)
        if  num % j == 0 : 
            is_prime=False
            break

    if is_prime == True:
        ans += 1

print(ans)
            


