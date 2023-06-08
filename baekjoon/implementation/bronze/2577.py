import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

num = A * B * C

result = [0 for _ in range(10)]

for i in str(num):
    result[int(i)] += 1

for i in result:
    print(i)