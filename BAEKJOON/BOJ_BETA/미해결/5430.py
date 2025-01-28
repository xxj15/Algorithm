#AC - 골드 5 
import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    AC = list(input().strip())  # 명령어 받음
    n = int(input())  # 배열에 들어있는 수의 개수

    if n == 0:  # 배열이 비어 있는 경우 처리
        if 'D' in AC:
            print('error')
            break
        else : 
            print('[]')
            break
    else:
        array_input = input().strip() 
        arr = list(map(int, array_input[1:-1].split(',')))  # 대괄호 제거, 쉼표 구분하여 숫자 리스트로 변환

    for order in AC:  # 명령어 처리
        if order == 'R':
            arr.reverse()
        elif order == 'D':   # 명령어가 'D'인 경우
            if not arr:  # 리스트가 빈 경우
                print("error")
                break
            else:
                arr.pop(0)  # 리스트에서 맨 앞에 있는 요소 제거

    else:
        # 출력 시 공백 없는 형식으로 변환
        print("[" + ",".join(map(str, arr)) + "]")
