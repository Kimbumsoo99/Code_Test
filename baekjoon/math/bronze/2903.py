import sys
input = sys.stdin.readline

N = int(input())

square = 1

for i in range(N):
    square *= 2
print((square+1) * (square+1))