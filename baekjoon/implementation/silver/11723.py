import sys
input = sys.stdin.readline

M = int(input())
S = []
for i in range(M):
    reg_data = list(map(str, input().split()))
    if len(reg_data) > 1:
        if reg_data[0] == "add":
            S += [reg_data[1]]
        elif reg_data[0] == "remove":
            if reg_data[1] in S:
                S.pop(S.index(reg_data[1]))
        elif reg_data[0] == "check":
            if reg_data[1] in S:
                print(1)
            else:
                print(0)
        elif reg_data[0] == "toggle":
            if reg_data[1] in S:
                S.pop(S.index(reg_data[1]))
            else:
                S += [reg_data[1]]
    else:
        if reg_data[0] == "all":
            S = [str(i+1) for i in range(20)]
        elif reg_data[0] == "empty":
            S = []

