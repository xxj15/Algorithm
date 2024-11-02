from collections import deque

def solution(n, wires):
    answer = 100000
    graph = [[] for _ in range(n+1)] # 0번부터 노드가 시작되는 것이 아니기 때문에 +1추가해주기!

    for s, e in wires: # 양방향이기 때문에 양쪽 모두 추가해주기
        graph[s].append(e)
        graph[e].append(s)

    for node1, node2 in wires:
        visited = [False for _ in range(n + 1)] # 모든 노드를 순회할 것이기 때문에 매 순회마다 방문 배열을 만들어줍니다
        q = deque()
        q.append(node1)
        result = 1
        visited[node1] = True # true를 넣어주는 이유는 여기서 시작할거니까요.
        visited[node2] = True # 여기에 넣어주는 이유는 한쪽만 돌거에요.

        while q:
            node = q.popleft()
            for ele in graph[node]:
                if not visited[ele]:
                    result += 1
                    visited[ele] = True
                    q.append(ele)

        # 여기서 최소값과 최대값을 구하고 업데이트합니다
        min_value = min(result, n-result)
        max_value = n - min_value
        if answer > max_value - min_value:
            answer = max_value - min_value

    return answer