import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    money = int(input())
    Q = money // 25
    money %= 25
    D = money // 10
    money %= 10
    N = money // 5
    money %= 5
    P = money // 1
    print(Q, D, N, P)