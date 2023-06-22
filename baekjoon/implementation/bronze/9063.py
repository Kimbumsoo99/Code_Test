import sys
input = sys.stdin.readline

N = int(input())

x1, y1, x2, y2 = 10000, 10000, -10000, -10000
for i in range(N):
    X, Y = map(int, input().split())
    if X < x1:
        x1 = X
    if X > x2:
        x2 = X
    if Y < y1:
        y1 = Y
    if Y > y2:
        y2 = Y
print(abs(x2-x1) * abs(y2-y1))