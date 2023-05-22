import sys

input = sys.stdin.readline

T = int(input())
stack = []
arr = []
check = 0
for i in range(0, T):
    arr += input().split()

for i in arr:
    # print("i=",i)
    for index, a in enumerate(i):
        if a == '(':
            stack.append(a)
            # print(stack)
        elif a == ')':
            if len(stack) < 1:
                check = -1
                break
            stack.pop()
            # print(stack)
    if len(stack) > 0 or check == -1:
        print("NO")
        check = 0
    else:
        print("YES")
    stack = []
