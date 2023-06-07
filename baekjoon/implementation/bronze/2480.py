import sys

input = sys.stdin.readline
N = list(map(int, input().split()))
N.sort()
if N[0] == N[-1]:
    print(10000 + N[0] * 1000)
elif N[0] == N[1] or N[1] == N[2]:
    print(1000 + N[1] * 100)
else:
    print(N[-1] * 100)

# a, b, c = sorted(input().split())
