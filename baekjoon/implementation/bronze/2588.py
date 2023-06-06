import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

o = M % 10
t = M // 10 % 10
h = M // 100

print(N * o)
print(N * t)
print(N * h)
print(N * M)

