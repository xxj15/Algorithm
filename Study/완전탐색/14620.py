import sys
input = sys.stdin.readline

N = int(input())
flowers = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]  # 오른쪽, 아래, 왼쪽, 위
dy = [0, 1, 0, -1]

def check(x1, y1, x2, y2):
    arr1 = set()
    arr2 = set()

    # (x1, y1)과 그 주변 좌표 저장
    arr1.add((x1, y1))
    for i in range(4):
        nx = x1 + dx[i]
        ny = y1 + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            arr1.add((nx, ny))

    # (x2, y2)와 그 주변 좌표 저장 
    arr2.add((x2, y2))
    for i in range(4):
        nx, ny = x2 + dx[i], y2 + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            arr2.add((nx, ny))

    # 두 영역이 겹치는지 확인
    if arr1 & arr2:
        return 0  # 겹침
    return 1  # 겹치지 않음

def check_3rd(x, y):  # 세 번째 꽃 심을 위치 체크
    min_cost = float('inf')

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 < nx < N-1 and 0 < ny < N-1):  # 범위를 벗어나면 0 반환
            continue

        if check(x, y, nx, ny) == 0:  # 겹치면 0 반환
            continue

        cost_3 = flowers[nx][ny]
        
        for j in range(4):  # 네 방향 비용 추가
            px= nx + dx[j]
            py = ny + dy[j]

            if not (0 <= px < N and 0 <= py < N):  # 범위 벗어나면 무효
                cost_3 = float('inf')
                break

        min_cost = min(min_cost, cost_3)

    return min_cost if min_cost != float('inf') else 0 


def check_2nd(x, y):  # 두 번째 꽃 심을 위치 체크
    min_cost = float('inf')

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        third_cost = check_3rd(nx, ny)
        if third_cost == 0:  # check_3rd == 0이면 즉시 0 반환
            continue

        if not (0 < nx < N-1 and 0 < ny < N-1): # 네 방향 중 하나라도 범위 벗어나면 0 반환
            continue

        if check(x, y, nx, ny) == 0:  # 겹치면 0 반환
            continue

        cost_2 = flowers[nx][ny]

        for j in range(4):  # 네 방향 비용 추가
            px= nx + dx[j]
            py = ny + dy[j]

            if not (0 <= px < N and 0 <= py < N):  # 범위 벗어나면 무효
                cost_2= float('inf')
                break

        cost_2 += third_cost
        min_cost = min(min_cost, cost_2)

    return min_cost if min_cost != float('inf') else 0 

ans = float('inf')
for i in range(1, N - 1):  # 꽃은 가장자리에 못 심음
    for j in range(1, N - 1):
        cost = flowers[i][j]
        
        for k in range(4):  
            cost += flowers[i + dx[k]][j + dy[k]] 
        total_cost = float('inf')

        second_cost = check_2nd(i, j)

        if second_cost != 0:
            total_cost = cost + second_cost
        
        ans = min(ans, total_cost)
        print(total_cost)
            

print(ans)
