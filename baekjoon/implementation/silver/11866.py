from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque()
for i in range(1, N+1):
    queue.appendleft(i)
count = 0
result = []
while len(result) < N:
    count += 1
    tmp = queue.pop()
    if count % K == 0:
        count = 0
        result.append(tmp)
    else:
        queue.appendleft(tmp)

print("<", end="")
for i in range(N - 1):
    print(result[i], end=", ")
print(str(result[-1]) + ">")