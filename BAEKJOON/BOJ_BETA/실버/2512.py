#예산 
import sys 
input = sys.stdin.readline

N = int(input())
money = list(map(int, input().split()))
total = int(input())

sum_money = sum(money)

# 예산 요청액이 총 예산보다 적은 경우 
if sum_money < total: 
    print(max(money))

else: 
    low, high = 0, max(money)
    ans = 0 

    while low<= high: 
        mid = (low+high)//2
        new_money = 0
        for m in money:     
            new_money += min(mid, m)

        if new_money <= total : 
            ans = mid 
            low = mid + 1
        else:
            high = mid - 1
    
    print(ans)
    
