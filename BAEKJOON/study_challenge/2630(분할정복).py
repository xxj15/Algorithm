# 색종이 만들기
import sys
input = sys.stdin.readline

N = int(input().strip()) 
square = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0 

def div(x, y, n):
    global white, blue

    start = square[x][y]
    same = all(square[i][j] == start for i in range(x, x + n) for j in range(y, y + n)) # 영역이 단일 색인지 확인 

    # 영역이 모두 단일색인 경우 
    if same:
        if start == 0:
            white += 1
        else:
            blue += 1

    # 4등분
    else:
        new_size = n // 2 
        div(x, y, new_size)           
        div(x, y + new_size, new_size)   
        div(x + new_size, y, new_size) 
        div(x + new_size, y + new_size, new_size) 

div(0, 0, N)

print(white)
print(blue)

