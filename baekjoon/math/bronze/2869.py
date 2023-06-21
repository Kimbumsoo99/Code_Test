import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

day_N = A - B
if (V - A) % day_N == 0:
    result = ((V - A) // day_N)
else:
    result = ((V - A) // day_N) + 1

print(result + 1)