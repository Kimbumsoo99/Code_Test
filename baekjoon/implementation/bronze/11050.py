import sys
input = sys.stdin.readline

N, K = map(int, input().split())
tmp_N, tmp_K = 1, 1
if K > N / 2:
    K = N - K

if K == 0:
    print(1)
else:
    for i in range(K):
        tmp_N *= (N - i)
        tmp_K *= (K - i)
    print(int(tmp_N / tmp_K))
