import sys
input = sys.stdin.readline
stack = []

N = int(input())

for i in range(N):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))