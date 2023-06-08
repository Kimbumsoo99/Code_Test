import sys
# from collections import deque

input = sys.stdin.readline

N = int(input())
level = []
# level = deque()

for i in range(N):
    level.append(int(input()))

level.sort()
# level = deque(sorted(level))

if N == 0:
    print("0")
else:
    tmp = int((N * 0.15 + 0.5) // 1)
    for i in range(tmp):
        level.pop()
        # level.popleft()
    level.sort(reverse=True)
    for i in range(tmp):
        level.pop()
    print(int((sum(level) / len(level) + 0.5) // 1))
