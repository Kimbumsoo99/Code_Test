import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

T = int(input())

for i in range(T):
    reg_data = list(map(str, input().split()))
    reg_data[0] = reg_data[0].strip()
    if len(reg_data) > 1:
        reg_data[1] = int(reg_data[1].strip())
        if reg_data[0] == "push_back":
            queue.append(reg_data[1])
        elif reg_data[0] == "push_front":
            queue.appendleft(reg_data[1])
    else:
        if reg_data[0] == "front":
            print(queue[0] if len(queue) > 0 else -1)
        elif reg_data[0] == "back":
            print(queue[-1] if len(queue) > 0 else -1)
        elif reg_data[0] == "size":
            print(len(queue))
        elif reg_data[0] == "empty":
            print(1 if len(queue) < 1 else 0)
        elif reg_data[0] == "pop_front":
            print(queue.popleft() if len(queue) > 0 else -1)
        elif reg_data[0] == "pop_back":
            print(queue.pop() if len(queue) > 0 else -1)
