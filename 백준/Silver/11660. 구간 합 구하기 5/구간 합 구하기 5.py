import sys 
input = sys.stdin.readline

n, q = map (int, input().split())
A = []
D = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)
        
for i in range (1, n+1):
    for j in range (1,n+1):
        D[i][j] = D[i][j-1]+D[i-1][j]-D[i-1][j-1]+A[i-1][j-1]
        
for _ in range (q):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1]+D[x1-1][y1-1]
    print(result)