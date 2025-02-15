#텀 프로젝트 - DFS + 사이클 
import sys
input = sys.stdin.readline

T = int(input())

stu = []
ans = []

for _ in range(T):
    n = int(input())

    team = [0] 
    team.extend(map(int, input().split()))  # extend 써야 리스트에 여러 개의 요소를 개별적으로 추가됨됨

    visited = [False] * (n + 1)
    finished = [False] * (n + 1)
    count = n

    stack = []
    
    for student in range(1, n + 1):
        if not visited[student]:
            current = student
            while not visited[current]:
                visited[current] = True
                stack.append(current)
                current = team[current]

            if current in stack:
                while stack:
                    student = stack.pop() # 사이클을 형성한 학생을 하나씩 꺼냄
                    count -= 1
                    if student == current:
                        break

            while stack:
                finished[stack.pop()] = True

    ans.append(str(count))

for result in ans:
    print(result)
