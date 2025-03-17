#동전 게임 
import sys
input = sys.stdin.readline
from collections import deque 

def flip(flippingCase, arr): 
    for num in flippingCase:
        arr[num] = 0 if arr[num] == 1 else 1
    return arr 

def bfs(array): 
    flip_cases = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

    visited = [False] * 512 
    visited[int(''.join(map(str, array)), 2)] = True  # 현재 array ([1, 1, 1, 1, 0, 1, 1, 1, 1]) 방문처리해주기  - 정수 리스트를 문자열로 변환환
    queue = deque([(int(''.join(map(str, array)), 2), 0)]) # 큐에 (현재 상태를 이진수 -> 십진수로 변환한 값, 현재 위치(깊이)) 저장. 

    while queue: 
        arr_decimal, cnt = queue.popleft()

        if arr_decimal == 0 or arr_decimal == 511:  # 모든 동전이 같은 면일 경우 종료
            return cnt 
        
        for case in flip_cases: 
            new_array = flip(case, list(map(int, bin(arr_decimal)[2:].zfill(9)))) # 현재 상태를 2진수 리스트로 변환 후 뒤집기
            # bfs 탐색을 위해 숫자로 변환했지만 다시 리스트로 변환해야 flip을 적용할 수 있기 때문
            newArr_decimal = int(''.join(map(str, new_array)), 2)

            if not visited[newArr_decimal]:
                visited[newArr_decimal] = True
                queue.append((int(''.join(map(str, new_array)), 2), cnt + 1))
    
    return -1  # 한 가지 면으로 설정할 수 없는 경우 

T = int(input())

for _ in range(T): 
    arr = [list(input().split()) for _ in range(3)]
    arr = [1 if arr[y][x] == 'H' else 0 for y in range(3) for x in range(3)]  # H: 1, T: 0 변환 (비트마스크)
    print(bfs(arr))



