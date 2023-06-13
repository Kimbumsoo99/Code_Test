import sys

input = sys.stdin.readline

T = int(input())
# T = 1


for i in range(T):
    K = int(input())  # 층 (행)
    N = int(input())  # 호 (열)

    apart = [[1 for b in range(N)] for a in range(K+1)]
    apart[0] = [b for b in range(1, N+1)]
    for j in range(1, K+1):
        for a in range(N):
            if a > 0:
                apart[j][a] = apart[j - 1][a] + apart[j][a - 1]
            else:
                apart[j][a] = 1
    print(apart[K][N-1])

