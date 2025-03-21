#암호 만들기 
import sys
from itertools import combinations

input = sys.stdin.readline

L, C = map(int, input().split())
word_list = input().split()
word_list.sort()  # 사전순 정렬을 위해 미리 정렬

# 조건: 모음 하나, 자음 두개 포함
vowels = {'a', 'e', 'i', 'o', 'u'}
m_word = []
j_word = []

for word in word_list:
    if word in vowels:
        m_word.append(word)
    else:
        j_word.append(word)

result = set()

# 모음 1개 선택
for m_comb in combinations(m_word, 1):
    # 자음 2개 선택
    for j_comb in combinations(j_word, 2):
        base_list = list(m_comb + j_comb)  # 지금까지 선택된 3개의 문자
        remaining_list = set(word_list) - set(base_list)  # 아직 안 쓴 문자들

        # 남은 문자 중에서 L - 3개 선택
        for rest_comb in combinations(remaining_list, L - 3):
            total = list(base_list + list(rest_comb))
            total.sort()
            result.add(''.join(total))

for ans in sorted(result):
    print(ans)
