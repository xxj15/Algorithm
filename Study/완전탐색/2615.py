#오목
import sys
input = sys.stdin.readline

dx = [1, 0, 1, -1]  
dy = [0, 1, 1, 1]

def check(color, x, y):
    for d in range(4):  
        count = 1
        nx, ny = x + dx[d], y + dy[d]
        
        while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
            count += 1
            if count == 5:
                # 육목 여부 확인
                px, py = x - dx[d], y - dy[d]
                qx, qy = nx + dx[d], ny + dy[d]
                
                if (0 <= px < 19 and 0 <= py < 19 and board[px][py] == color):
                    break
                if (0 <= qx < 19 and 0 <= qy < 19 and board[qx][qy] == color):
                    break
                return (True, x + 1, y + 1)  
            
            nx += dx[d]
            ny += dy[d]
    
    return (False, None, None)

board = [list(map(int, input().split())) for _ in range(19)]

winner = None
winner_x, winner_y = None, None
cnt_black, cnt_white = 0, 0

for x in range(19):
    for y in range(19):
        if board[x][y] in [1, 2]:
            win, wx, wy = check(board[x][y], x, y)
            if win:
                if board[x][y] == 1:
                    cnt_black += 1
                else:
                    cnt_white += 1
                
                winner = board[x][y]
                winner_x, winner_y = wx, wy

if cnt_black > 1 or cnt_white > 1 or cnt_white == cnt_black:
    print(0)
elif winner:
    print(winner)
    print(winner_x, winner_y)
else:
    print(0)
