from collections import deque
import sys

input = sys.stdin.readline

test = int(input())
printer = deque()

for i in range(0, test):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    for j in range(0, len(priority)):
        printer.appendleft(priority[j])
    count = 1

    while True:
        if printer[-1] == max(printer) and M == 0:  # 중요도가 가장 높은게 M이면 출력 후 종료
            print(count)
            break

        if printer[-1] == max(printer):  # 중요도가 가장 높다면 인쇄
            printer.pop()
            count += 1
        else:
            temp = printer.pop()  # 중요도가 낮다면 다시 Queue 삽입
            printer.appendleft(temp)

        M -= 1
        if M < 0:
            M = len(printer) - 1
    printer.clear()

