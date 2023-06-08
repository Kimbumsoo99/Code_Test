import sys
input = sys.stdin.readline

N = int(input())

numbers = input()
sum = 0
for i in numbers:
    if i != "\n":
        sum += int(i)

print(sum)