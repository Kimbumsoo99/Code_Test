import sys

input = sys.stdin.readline

N = int(input())

commands = []
stack = []

for i in range(0, N):
    commands.append(input().split())

for command in commands:
    # print(command[0])
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "top":
        if len(stack) <= 0:
            print(-1)
            continue
        print(stack[-1])
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "pop":
        if len(stack) <= 0:
            print(-1)
            continue
        print(stack.pop())
    elif command[0] == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)
