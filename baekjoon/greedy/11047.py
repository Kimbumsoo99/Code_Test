import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
for i in range(0, N):
    coins.append(int(input()))

coins.sort()


count = 0
# coins.pop()
coin = coins.pop()
while K:
    # if K % coin == 0:
    #    count += K // coin
    #    break
    if K >= coin:
        count += K // coin
        K %= coin
        # K -= coin
        # count += 1
    else:
        coin = coins.pop()
print(count)
