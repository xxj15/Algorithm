# 퇴사 
import sys 
input = sys.stdin.readline 

max_price = 0  

def dfs(day, total_price): 
    # dfs()가 재귀적으로 탐색하면서 전역 변수(max_price)를 갱신하는 방식으로 동작.
    global max_price 

    if day > N : 
        return 
    
    max_price = max(max_price, total_price)

    for date in range(day, N):
        days, price = counsel_list[date]

        if date + days <= N : # 현재 날짜와 소요 시간이 N보다 작음 (N보다 적은 시간 안에 상담 종료될 수 있음음)
            dfs(date + days, price + total_price)

N = int(input())
counsel_list = [list(map(int, input().split()))for _ in range(N)]

dfs(0, 0)

print(max_price)