# 좋은 수열 
import sys
input = sys.stdin.readline

n = int(input())
ans = []

# 숫자 1, 2, 3만으로 이루어진 수열 
def check(sequence):
    length = len(sequence)
    for i in range(1, length // 2 + 1):  
        if sequence[-i:] == sequence[-2 * i:-i]: 
            return -1 
    return 0 

def dfs(depth):
    if depth == n:  # 원하는 길이에 도달했으면 출력
        print(''.join(map(str, ans)))
        exit(0)  # 프로그램 종료
    
    for x in range(1, 4):  # 1, 2, 3을 시도
        ans.append(x)  # 값을 추가
        if check(ans) == 0:  # 좋은 수열이면
            dfs(depth + 1)  # 다음 단계로 재귀 호출
        ans.pop()  # 값을 제거하여 백트래킹

dfs(0)