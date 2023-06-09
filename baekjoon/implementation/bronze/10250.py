import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    YY, XX = 0, 0
    H, W, N = map(int, input().split())
    if N % H == 0:
        YY = H
        XX = N // H
    else:
        YY = N % H
        XX = N // H + 1

    if XX < 10:
        XX = "0" + str(XX)
    print(str(YY) + str(XX))
