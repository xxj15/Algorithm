#정수 삼각형
import sys
input = sys.stdin.readline

n = int(input())
triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1, n): 
    for j in range(len(triangle[i])):
        if j == 0:  # 왼쪽 끝 
            triangle[i][j] += triangle[i - 1][j]
        elif j == len(triangle[i]) - 1:  # 오른쪽 끝
            triangle[i][j] += triangle[i - 1][j - 1]
        else:  # 중간 값 
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

print(max(triangle[-1]))  # 마지막줄에서 최댓값 출력
