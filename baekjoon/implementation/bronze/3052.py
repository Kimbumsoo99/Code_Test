import sys
input = sys.stdin.readline

T = set()

for i in range(10):
    T.add(int(input()) % 42)

print(len(T))