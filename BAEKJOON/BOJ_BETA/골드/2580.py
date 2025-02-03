# 스도쿠 (백트래킹)
import sys
input = sys.stdin.readline

# 스도쿠 입력받기
arr = [] 
for _ in range(9):
    row = list(map(int, input().split()))  
    arr.append(row)  


# 가로, 세로, 사각형 각각 확인 
def row(x, num):
    for y in range(9): 
        if arr[x][y] == num:
            return 0
    return 1 

def column(y, num):
    for x in range(9):  
        if arr[x][y] == num:  
            return 0
    return 1

def square(x, y, num):
    start_x, start_y = (x // 3) * 3, (y // 3) * 3
    for i in range(3): 
        for j in range(3): 
            if arr[start_x + i][start_y + j] == num:  
                return 0
    return 1


def dfs():
    for i in range(9):  
        for j in range(9):  
            if arr[i][j] == 0: 
                for num in range(1, 10): 
                    if row(i, num) and column(j, num) and square(i, j, num):
                        arr[i][j] = num 
                        if dfs(): # 재귀호출로 다음 빈칸 탐색! 
                            return True 
                        arr[i][j] = 0 # 다음 단계에서 호출 실패시 되돌아가기 
                return False # 가능한 모든 숫자를 매칭해봤지만 실패함 
    return True 

dfs()

for row in arr: 
    print(' '.join(map(str, row)))  