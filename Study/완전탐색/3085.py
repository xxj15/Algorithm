#사탕 게임 
import sys 
input = sys.stdin.readline

def Max_candies(board):
    max_candies = 0 

    # 행 검사 
    for i in range(N):
        cnt = 1 
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else :
                cnt = 1
            max_candies = max(max_candies,cnt)

    # 열 검사 
    for j in range(N):
        cnt = 1 
        for i in range(1, N):
            if board[i][j] == board[i-1][j]:
                cnt += 1
            else :
                cnt = 1
            max_candies = max(max_candies,cnt)

    return max_candies


N = int(input())
candies = [list(input().strip()) for _ in range(N)] 

dx = [1, 0]
dy = [0, 1]

ans = Max_candies(candies)

for x in range(N):
    for y in range(N):
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N : # 범위 제한 
                # 교환 
                candies[x][y], candies[nx][ny] = candies[nx][ny], candies[x][y]

                ans = max(ans, Max_candies(candies))

                # 원상복구 
                candies[x][y], candies[nx][ny] = candies[nx][ny], candies[x][y]


print(ans)