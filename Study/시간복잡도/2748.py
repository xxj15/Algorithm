#피보나치 수 2
import sys
input = sys.stdin.readline

N = int(input())

fib_num=[0]*(N+1)
fib_num[0]=0
fib_num[1]=1

for i in range(2,N+1):
    fib_num[i] = fib_num[i-2]+fib_num[i-1]

print(fib_num[N])