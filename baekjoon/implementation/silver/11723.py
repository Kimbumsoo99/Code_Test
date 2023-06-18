import sys
input = sys.stdin.readline

M = int(input())
S = 0
for i in range(M):
    reg_data = list(map(str, input().split()))
    if len(reg_data) > 1:
        reg_data[1] = int(reg_data[1])
        if reg_data[0] == "add":
            S = S | (1 << reg_data[1])
        elif reg_data[0] == "remove":
            S = S & ~(1 << reg_data[1])
        elif reg_data[0] == "check":
            if S & (1 << reg_data[1]):
                print(1)
            else:
                print(0)
        elif reg_data[0] == "toggle":
            S ^= (1 << reg_data[1])
    else:
        if reg_data[0] == "all":
            S = (1 << 21) - 1
        elif reg_data[0] == "empty":
            S = 0

