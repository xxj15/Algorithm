# 숫자 야구 
import sys
input = sys.stdin.readline
from itertools import permutations

def count(questions):
    possible_nums = list(permutations(range(1, 10), 3))  # 1~9 중 3개를 선택하는 모든 경우의 수
    
    def score(target, guess):
        strike, ball = 0, 0
        for i in range(3):
            if target[i]== guess[i]:
                strike += 1
            elif guess[i] in target:
                ball += 1
        return strike, ball
    
    valid_numbers = []
    for num in possible_nums:
        valid = True
        for guess, s, b in questions:
            if score(num, guess) != (s, b):
                valid = False
                break
        if valid:
            valid_numbers.append(num)
    
    return len(valid_numbers)

N = int(input())
questions = [list(map(int, input().split())) for _ in range(N)]

for q in questions:
    q[0] = list(map(int, str(q[0]))) 

print(count(questions))
