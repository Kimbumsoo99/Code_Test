import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

num = sorted([A, B, C])
print(num[1])