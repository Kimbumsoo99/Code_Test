# 백준 11660번 구간합2
# 2차원 배열에서의 구간 합 구하기

# 2차원 배열의 구간합을 구하는 공식
# 1행과 1열은 D[i][1] = D[i-1][1]+A[i][1] / D[1][j] = D[1][j-1]+A[1][j]
# 이외 행은 구간합 + 구간합 - 중복구간합 + 현재위치값이므로
# D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 2차원 배열 구간합을 통해 특정 위치의 구간합 구하기
# 2 2 3 4라면 D[1][4]와 D[3][1]까지는 포함이 안되므로 제외하고 이때 중복하여 뺀 값 D[1][1]을 더한다.
# SUM = D[3][4] - D[1][4] - D[3][1] + D[1][1]
# SUM = D[X2][Y2] - D[X1-1][Y2] - D[X2][Y1-1] + D[X1-1][Y1-1]

# 1번째 입력 표의 크기 N과 합을 구해야하는 횟수 M
# 2번째 입력부터는 N개의 줄에 표에 채워진 숫자를 채운다.
# 이후 입력에는 M 횟수에 대한 값을 구한다. 이때 좌표는 X1 Y1 X2 Y2 순으로 입력한다.


import sys

input = sys.stdin.readline
n, m = map(int, input().split())
A = [[0]*(n+1)]
D = [[0]*(n+1) for _ in range(n+1)]
for i in range(0, n):
    A_row = [0]+[int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for i in range(m):
    X1, Y1, X2, Y2 = map(int, input().split())
    result = D[X2][Y2] - D[X1-1][Y2] - D[X2][Y1-1] + D[X1-1][Y1-1]
    print(result)
