import sys
input = sys.stdin.readline

chess = []
count = 0
for i in range(8):
    chess.append(input().rstrip())
    for j in range(4):
        # print(chess[i], chess[i][2*j])
        if i % 2 == 0 and chess[i][2*j] == "F":
            count += 1
        elif i % 2 != 0 and chess[i][2*j+1] == "F":
            count += 1

print(count)