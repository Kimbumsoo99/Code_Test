import sys
from collections import deque

input = sys.stdin.readline

circle_table = deque()

N, K = map(int, input().split())
count = 0

result = []
for i in range(1, N + 1):
    circle_table.appendleft(i)
# print(circle_table)

while N > 0:
    for i in range(K - 1):
        person = circle_table.pop()
        circle_table.appendleft(person)
        # print(circle_table)
    result.append(circle_table.pop())
    # print(result)
    N -= 1

# print("<", end="")
# for i in range(len(result) - 1):
#     print(str(result[i]) + ", ", end="")
# print(str(result[len(result) - 1]) + ">")

print(f"<{', '.join(map(str, result))}>")