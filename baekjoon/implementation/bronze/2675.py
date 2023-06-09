import sys
input = sys.stdin.readline

T = int(input())
P = ""
test = []
for i in range(T):
    R, S = map(str, input().split())
    S = S.rstrip()
    for j in S:
        for k in range(int(R)):
            P += j
    test.append(P)
    P = ""
for i in range(T):
    print(test[i])