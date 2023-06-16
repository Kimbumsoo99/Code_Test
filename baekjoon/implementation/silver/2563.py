import sys
input = sys.stdin.readline

N = int(input())
width = set()


for i in range(N):
    X, Y = map(int, input().split())
    for x in range(X, X+10):
        for y in range(Y, Y+10):
            width.add((x, y))

print(len(width))
