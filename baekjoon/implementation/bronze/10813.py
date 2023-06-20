import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num_arr = [i + 1 for i in range(N)]


for i in range(M):
    A, B = map(int, input().split())
    num_arr[A - 1], num_arr[B - 1] = num_arr[B - 1], num_arr[A - 1]
for i in num_arr:
    print(i, end=" ")