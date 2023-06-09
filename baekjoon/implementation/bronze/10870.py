import sys

input = sys.stdin.readline

N = int(input())

num_array = [0, 1]
for i in range(N - 1):
    num_array.append(num_array[i] + num_array[i + 1])
print(num_array[N])
