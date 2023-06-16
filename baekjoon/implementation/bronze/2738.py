import sys
input = sys.stdin.readline

N, M = map(int, input().split())

result = []

for n in range(2):
    for i in range(N):
        if n == 0:
            result.append(list(map(int, input().split())))
        else:
            tmp = list(map(int, input().split()))
            for j in range(M):
                result[i][j] += tmp[j]

for i in range(N):
    for j in range(M):
        print(result[i][j], end=" ")
    print()