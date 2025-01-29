import sys 
input = sys.stdin.readline

while True:
        line = input().strip()
        data = list(map(int, line.split()))

        k = data[0] # 골라야하는 숫자 개수 
        s = data[1:] # 후보 숫자들
        if data[0] == 0:
            break

        