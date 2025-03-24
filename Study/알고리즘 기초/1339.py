#단어 수학
import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
words = [input().strip() for _ in range(n)]

weight = defaultdict(int)

# 각 알파벳의 자릿수 가중치 계산
for word in words:
    length = len(word)
    for i, char in enumerate(word):
        weight[char] += 10 ** (length - i - 1)

# 가중치 기준으로 정렬
sorted_chars = sorted(weight.items(), key=lambda x: -x[1])

# 9부터 숫자 할당
num = 9
char_to_digit = {}
for char, _ in sorted_chars:
    char_to_digit[char] = num
    num -= 1

# 단어를 숫자로 변환하고 합 계산
total = 0
for word in words:
    converted = ''.join(str(char_to_digit[char]) for char in word)
    total += int(converted)

print(total)
