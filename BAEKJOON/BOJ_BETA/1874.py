import sys
input = sys.stdin.readline

n = int(input())

# 입력받은 문자열을 int()로 정수로 변환 -> 리스트 형식으로 
sequence = [int(input()) for _ in range(n)] # 반복문은 n번 실행되며, 각 반복마다 input()을 호출해 값을 입력받음
stack = []
result = []
cur = 1

for i in sequence : 
    while cur <= i :
        stack.append(cur)
        result.append("+")
        cur += 1

    if stack[-1] == i:
        stack.pop()
        result.append("-")

    else : 
        print("NO")
        break

else :
    for i in result:
        print(i)


    
