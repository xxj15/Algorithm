# 9095번: 1,2,3 더하기 
# DP 
import sys
input = sys.stdin.readline

n = int(input())

# 규칙 찾기 
# T = 1이면 1 , T = 2 이면 2 (2, 1+1) , T = 3 이면 4 (3, 1+2, 2+1, 1+1+1) 
# T = 4 이면 7 (4, 1+3, 2+2, 3+1, 1+1+2, 1+2+1, 2+1+1, 1+1+1+1) = 4 + 2 + 1
# T = 4, 5, 6 ... 이상이면 T[i] = T[i-1] + T[i-2] + T[i-3] 

for _ in range(n):
    N = int(input())
    T=[0]*(N+1)

    for i in range(1, N+1):
        if i == 1 :
            T[i] = 1
        elif i == 2:
            T[i] = 2
        elif i == 3 :
            T[i] = 4
        else : 
            T[i]=T[i-1]+T[i-2]+T[i-3]

    print(T[N])