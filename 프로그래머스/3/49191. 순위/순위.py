def solution(n, results):
    answer = 0
    # 각 선수의 승패 관계를 저장할 집합 리스트
    win = [set() for i in range(n + 1)]  # i 선수가 이긴 상대 선수들을 저장
    lose = [set() for i in range(n + 1)]  # i 선수가 진 상대 선수들을 저장
    
    # 주어진 결과를 바탕으로 승리 및 패배 관계 설정
    for a, b in results:
        win[a].add(b)  # a 선수가 이긴 선수 b를 win[a]에 추가
        lose[b].add(a)  # b 선수가 진 선수 a를 lose[b]에 추가
            
    # 승리와 패배 관계를 확장하여 간접 승패 관계 추가
    for idx in range(1, n + 1):
        # idx 선수가 이긴 선수 x는 idx가 진 선수들도 이긴 것으로 간주
        for x in win[idx]:
            lose[x].update(lose[idx])  # x 선수가 idx가 진 선수들을 모두 이기도록 갱신
        # idx 선수가 진 선수 x는 idx가 이긴 선수들도 진 것으로 간주
        for x in lose[idx]:
            win[x].update(win[idx])  # x 선수가 idx가 이긴 선수들을 모두 진 것으로 갱신
            
    # 각 선수별로 승패 관계를 계산하여 순위가 확실한지 확인
    for player in range(1, n + 1):
        count = len(win[player]) + len(lose[player])  # 승리와 패배 관계 합산
        if count == n - 1:  # 모든 다른 선수와의 승패 관계가 정해진 경우
            answer += 1  # 순위가 확실한 선수로 간주하여 카운트 증가
            
    return answer  # 순위가 확실한 선수 수 반환
