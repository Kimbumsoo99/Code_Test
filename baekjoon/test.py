import sys

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline()) #층
    n = int(sys.stdin.readline()) #호
    count = 0
    arr = [[0] * n for i in range(k+1)]
    temp = 0
    for j in range(k+1):
        arr[j][0] = 1

    for i in range(1,n):
        temp = 0
        for j in range(k+1):
            temp += arr[j][i-1]
            arr[j][i] = (temp + 1)

    count = arr[k][n-1]
    print(count)