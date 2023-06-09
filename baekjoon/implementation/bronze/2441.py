import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    for k in range(0, i):
        print(" ", end="")
    for j in range(N, i, -1):
        print("*", end="")
    print()