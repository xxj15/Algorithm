#유레카 이론 
import sys 
input = sys.stdin.readline 

triangle_nums = []
num = 0 
n = 1

# 삼각수 미리 저장 
while True: 
    num = int(n*(n+1)/2)
    if(num>1000):
        break
    triangle_nums.append(num)
    n +=1 


def eureka(M):
    for i in triangle_nums:
        for j in triangle_nums:
            for k in triangle_nums:
                if i + j + k == M :
                    return 1
                
    return 0


# 결과 출력 
T = int(input())

for i in range(T):
    M = int(input())
    print(eureka(M))
