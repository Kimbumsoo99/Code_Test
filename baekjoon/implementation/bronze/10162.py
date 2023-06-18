import sys
input = sys.stdin.readline

A, B, C = 300, 60, 10
T = int(input())
count = [0, 0, 0]
if T % C != 0:
    print(-1)
else:
    count[0] = T // A
    T %= A
    count[1] = T // B
    T %= B
    count[2] = T // C
    T %= C
    print(count[0], count[1], count[2])