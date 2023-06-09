import sys
input = sys.stdin.readline

N = int(input())

num_array = []
for i in range(N):
    num_array.append(int(input()))

num_array = sorted(num_array)

for i in num_array:
    print(i)