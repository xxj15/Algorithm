# 카드 정렬하기 
import sys 
input = sys.stdin.readline

N = int(input())
cards = [int(input()) for _ in range(N)]
cards.sort()
ans = 0 

for _ in range(N-1):
    if len(cards)>2:
        new = cards.pop(0) + cards.pop(0)
        ans += new 

        cards.append(new)
        cards.sort()
    
    else: 
        ans += sum(cards)

print(ans)


