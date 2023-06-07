import sys

input = sys.stdin.readline

num_array = []
for i in range(9):
    num_array.append(int(input()))

print(max(num_array))
for i in range(9):
    if max(num_array) == num_array[i]:
        print(i + 1)
        break
