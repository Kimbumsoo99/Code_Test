import sys
input = sys.stdin.readline

N = []
for i in range(3):
    N.append(list(map(int, input().split())))

for i in N:
    count = 0
    for j in i:
        if j == 0:
            count += 1
    if count == 0:
        print("E")
    elif count == 1:
        print("A")
    elif count == 2:
        print("B")
    elif count == 3:
        print("C")
    else:
        print("D")