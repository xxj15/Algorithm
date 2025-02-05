# 소수의 연속합
import sys
input = sys.stdin.readline

# 소수 목록 
MAX_N =  4000000
prime_check = [True] * (MAX_N + 1)
prime_check[0] = prime_check[1] = False 

for i in range(2, int(MAX_N ** 0.5) + 1):
    if prime_check[i]: 
        for j in range(i * i, MAX_N + 1, i):  
            prime_check[j] = False

n = int(input())
prime=[]

for i in range(n+1):
    if prime_check[i]==True and i<=n:
        prime.append(i) # n 보다 작은 소수 리스트 

# 투포인터 이용

left, right = 0, 0
sum_val = 0
ans=0

if n in prime:
    ans+=1 

while right < len(prime):
    if sum_val < n:
        sum_val += prime[right]
        right += 1  
    elif sum_val > n:
        sum_val -= prime[left]
        left += 1  
    else:  # sum_val == n
        ans += 1
        sum_val -= prime[left]
        left += 1

print(ans)




