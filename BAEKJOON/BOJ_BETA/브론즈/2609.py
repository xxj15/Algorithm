# 최대공약수와 최소공배수 
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
a = max(n,m)
b = min(n,m)


# 최대공약수 구하기 
for i in range(b):
    if n % b !=0 or m % b != 0 : 
        b-=1
    else : 
        print(b)
        break

# 최소공배수 구하기 
while True: 
    if a % n == 0 and a % m == 0:
        print(a)
        break
    a+=1