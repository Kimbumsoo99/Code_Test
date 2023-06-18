import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    b = b % 4 if b % 4 != 0 else 4
    result = (a ** b) % 10
    print(result if result != 0 else 10)
