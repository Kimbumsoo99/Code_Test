import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
num_arr = []
for i in range(M, N+1):
    if int(i / 2) + 1 == 2:
        num_arr.append(i)
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            break
        elif j == int(i / 2):
            num_arr.append(i)
if len(num_arr) > 0:
    print(sum(num_arr))
    print(min(num_arr))
else:
    print(-1)
