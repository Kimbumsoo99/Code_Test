import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

length = sorted([a, b, c], reverse=True)

if length[0] < length[1] + length[2]:
    print(sum(length))
else:
    print(length[1] + length[2] + length[1] + length[2] - 1)