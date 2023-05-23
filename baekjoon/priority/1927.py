import heapq as hq
import sys
input = sys.stdin.readline

N = int(input())
pq = []
result = []
for i in range(N):
    op = int(input())
    if op == 0:
        if len(pq) <= 0:
            result.append(0)
        else:
            num = hq.heappop(pq)
            result.append(num)
    else:
        hq.heappush(pq, op)

for i in result:
    print(i)