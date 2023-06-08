import sys
input = sys.stdin.readline

N, X = map(int, input().split())

smalls = []
numbers = list(map(int, input().split()))

for i in numbers:
    if X > i:
        print(i, end=" ")