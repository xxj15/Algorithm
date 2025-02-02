import sys 
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

# 로또 조합을 찾는 재귀 함수
def lotto(arr, idx, depth):
    if depth == 6:# 6개의 숫자를 선택했을 경우 더이상의 선택 없이 출력
        k = ' '.join(tmp) 
        if k not in visited:  # 선택된 숫자들이 중복된 조합인지 확인하고, 새로운 조합인 경우에만 프린트
            visited[k] = 1  # 이미 출력된건지 체크- 딕셔너리 
            print(k) 
        return

    # 현재 인덱스부터 끝까지 숫자 선택
    for i in range(idx, int(n)):
        tmp.append(arr[i])  # 숫자 추가
        lotto(arr, i + 1, depth + 1)  # 다음 숫자 선택을 위해 재귀 호출
        tmp.pop()  # 백트래킹: 이전 상태로 되돌리기


# 여러 테스트케이스를 처리하기 위한 루프
while True:
    data = input().split()  # 한 줄을 공백 기준으로 나눠 리스트로 저장
    n = data[0]  # 첫 번째 값 (문자열 형태)
    k = data[1:]  # 나머지 값들 (리스트 형태)

    if n == "0":  # 입력이 0이면 종료
        break
    visited = dict()  # 중복된 조합을 방지하기 위한 딕셔너리
    tmp = []  # 현재 선택된 숫자를 저장하는 리스트
    lotto(k, 0, 0)  # 로또 조합 생성 시작
    print()  # 테스트케이스 간 구분을 위한 개행 출력
