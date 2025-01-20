import sys 
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split())) # 가지고 있는 카드 
cnt = {}

for card in cards: 
    if card in cnt : 
        cnt[card]+=1
    else :
        cnt[card]=1

m = int(input())
check_nums = list(map(int, input().split()))

result = []

for num in check_nums:
    if num in cnt:
        result.append(cnt[num])
    else:
        result.append(0)

print(" ".join(map(str, result)))