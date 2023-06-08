import sys
input = sys.stdin.readline

N, M = map(int, input().split())

basket = [0 for _ in range(N)]

for i in range(M):
    turn = list(map(int, input().split()))
    for i in range(turn[0] - 1, turn[1]):
        basket[i] = turn[2]

for i in basket:
    print(i, end=" ")