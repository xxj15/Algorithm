#게임 
import sys, math
input = sys.stdin.readline

X, Y = map(int, input().split()) # X : 게임 횟수, Y : 이긴 게임 

Z = math.floor((Y*100/X)) # 현재 승률 

if Z > 99 : 
    print(-1)


else: 
    left = 1
    right = 1000000000
    ans = -1

    while left<= right:
        mid = (left + right)//2
        new_Z = math.floor(((Y + mid)*100) / (X + mid))

        if new_Z > Z : 
            ans = mid 
            right = mid -1 
            
        else:
            left = mid + 1
        
    print(ans)
