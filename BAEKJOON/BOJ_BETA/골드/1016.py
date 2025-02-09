#제곱 ㄴㄴ수 
import sys
input = sys.stdin.readline

min, max = map(int, input().split())

check = [True] * (max - min+1)

n = 2 
while n**2 <= max:
    square = n**2  # 현재 제곱수
    # 제곱수의 배수 중 min 이상인 첫 번째 수를 찾음
    if min % square == 0:
        start = min
    else:
        start = min + (square - min % square)

    for i in range(start, max + 1, square):  # square 간격 = 제곱수 배수들이라는 뜻 
        check[i-min] = False  # i-min인 이유는 check 배열의 크기 때문! 
    n += 1


print(sum(check))
