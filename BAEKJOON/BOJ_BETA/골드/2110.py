# 공유기 설치 
import sys 
input = sys.stdin.readline

N, C = map(int, input().split())
homes = [int(input()) for _ in range(N)]

homes.sort()

idx = 0 # 시작 인덱스 (첫번째 집에서 시작)

close = 1 # 가장 가까운 공유기 사이 거리 (최소 = 1)
far = homes[N-1]-homes[0] # 가장 먼 공유기 사이 거리 
ans = 1 

while close <= far : 
    mid = (close + far) // 2
    cnt = 1 # 설치한 공유기 수 
    idx = 0

    for i in range(1,N) :
        if homes[i]-homes[idx]>=mid: # 설치한 고유기 사이 거리가 현재 기준인 mid보다 크거나 같음 
            cnt += 1 
            idx = i # 기준이 되는 idx를 현재 인덱스로 갱신 
    
    if cnt >= C : 
        ans = mid 
        close = mid + 1
    
    else :
        far = mid -1 


print(ans)
