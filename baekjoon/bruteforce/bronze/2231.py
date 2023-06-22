import sys
input = sys.stdin.readline

N = int(input())
answer = 0

# length = len(str(N))
# start = N - length * 9
# for i in range(start, N):
for i in range(N):
    sum = 0
    tmp = i
    while tmp > 0:
        sum += (tmp % 10)
        tmp //= 10
    if N == i + sum:
        answer = i
        break
print(answer)
