from collections import deque
import sys
input = sys.stdin.readline

n=int(input())

queue = deque([_ + 1 for _ in range(0,n)])

if n==1:
    print(queue.pop())
else:
    while(True):
        queue.popleft()
        if(len(queue)<=1):
            break
        temp=queue.popleft()
        queue.append(temp)
    print(queue.pop())