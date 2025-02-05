#골드바흐의 추측 
import sys
input = sys.stdin.readline

#미리 소수 판별해두기 - 에라토스테네스의 체 
MAX_N = 1000000  
prime_check = [True] * (MAX_N + 1)
prime_check[0] = prime_check[1] = False  # 0과 1은 소수가 아님

for i in range(2, int(MAX_N ** 0.5) + 1):
    if prime_check[i]: 
        for j in range(i * i, MAX_N + 1, i):  # i의 배수들을 모두 False로 처리
            prime_check[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    find = False
    for a in range(3, n // 2 + 1, 2):  
        b = n - a
        if prime_check[a] and prime_check[b]:  # O(1)
            print(f"{n} = {a} + {b}")
            find = True
            break

    if not find:
        print("Goldbach's conjecture is wrong.")



'''
시간초과 
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1

while True:
    n = int(input())
    if n == 0:
        break

    find = False
    for a in range(3, n // 2 + 1, 2):  # 3부터 n//2까지 홀수만 검사 (1은 소수가 아니고, a = 2이면 b는 무조건 짝수니까 )
        b = n - a
        if is_prime(a) and is_prime(b):
            print("{} = {} + {}".format(n, a, b))
            find = True # 정답 찾으면 종료!!
            break  
    if not find:
        print("Goldbach's conjecture is wrong.")
'''

