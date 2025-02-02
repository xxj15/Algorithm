import sys 
input = sys.stdin.readline 

# 로또 조합을 찾는 재귀 함수
def lotto(arr, idx, depth):
    if depth == 6:# 6개의 숫자를 선택했을 경우 더이상의 선택 없이 출력
        k = ' '.join(tmp) 
        if k not in visited:  # 선택된 숫자들이 중복된 조합인지 확인하고, 새로운 조합인 경우에만 프린트
            visited[k] = 1  # 이미 출력된건지 체크- 딕셔너리 
            print(k) 
        return

    for i in range(idx, int(n)):
        tmp.append(arr[i])  
        lotto(arr, i + 1, depth + 1)  # 다음 숫자 선택을 위해 재귀 호출
        tmp.pop()  # 백트래킹을 하기 위해 마지막으로 추가한 숫자를 제거


while True:
    data = input().split()  
    n = data[0]  
    k = data[1:]  

    if n == "0":  
        break

    visited = dict()  # 이미 출력된 조합 저장!
    tmp = []  # 현재 조합 저장 
    lotto(k, 0, 0)  # k = 숫자 리스트 / idx = 0 처음부터 탐색 / depth = 0 현재까지 선택산 숫자 개수 
    print() 
