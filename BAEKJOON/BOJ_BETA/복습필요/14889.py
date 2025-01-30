#스타트와 링크
import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())

#  N개의 행을 입력받아, 각 행을 정수 리스트로 변환한 후 2차원 리스트로 저장
score = [list(map(int, input().split())) for _ in range(n)]

players = list(range(n)) 
ans = float('inf') # 변수를 무한대 (아주 큰 값)으로 초기화

# 가능한 팀 조합을 N/2명씩 생성 (절반만 구하면 나머지는 자동으로 정해짐)
for start in combinations(players, n // 2): 
    link = list(set(players) - set(start))  # set : 중복을 허용하지 않고, 순서가 없는 자료형형
    
    start_score = sum(score[i][j] + score[j][i] for i, j in combinations(start, 2))
    link_score = sum(score[i][j] + score[j][i] for i, j in combinations(link, 2))
    
    ans = min(ans, abs(start_score - link_score))
    
    if ans == 0: # 차이가 0이면 최적의 경우 
        break

print(ans)