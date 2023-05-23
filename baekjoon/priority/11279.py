import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
pq = []
for i in range(N):
    op = int(input())
    if op == 0:
        if len(pq) <= 0:
            print(0)
        else:
            print(hq.heappop(pq)[1])
    else:
        hq.heappush(pq, [-op, op])
