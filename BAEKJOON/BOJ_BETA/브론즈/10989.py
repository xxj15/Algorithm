import sys
input= sys.stdin.readline

n = int(input())

# a = list(int(input()) for _ in range(n))
# 입력 수 최대 개수 : 10,000,000개 => 너무 큼 
# 따라서 한 번에 list 안에 넣으면 메모리 너무 많이 잡아먹음 

num_arr = [0]*10001

for _ in range(n):
    num = int(input())
    num_arr[num]+=1

for i in range(10001):
    if num_arr[i]>=1:
        for _ in range (num_arr[i]):
            print(i)