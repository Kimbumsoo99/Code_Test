from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
board = [[0 for j in range(N + 1)] for i in range(N + 1)]
# arr = [[0 for j in range(cols)] for i in range(rows)]

K = int(input())
for i in range(0, K):
    a, b = input().split()
    board[int(a)][int(b)] = 'A'

L = int(input())
wayList = {}
for i in range(0, L):
    X, way = input().split()
    wayList[int(X)] =  way

cntTime = 0

snake = deque()
way = 0
row, col = 1, 1
snake.appendleft([row, col])

print(board)
print(len(board),len(board[0]))

# 게임시작
while True:
    cntTime += 1
    print("시간 ", cntTime)

    if way == 0:
        col += 1
    elif way == 1:
        row += 1
    elif way == 2:
        col -= 1
    elif way == 3:
        row -= 1

    if col > len(board[0]) - 1 or col < 0 or row > len(board) - 1 or row < 0:
        print(cntTime)
        print("벽에 부딪혀 게임 종료")
        break
    print(board[row][col])
    if board[row][col] != 'A':
        snake.appendleft([row, col])
        print(snake.pop())
    else:
        print("사과 발견 냠")
        snake.appendleft([row, col])

    if cntTime in wayList.keys():
        if wayList[cntTime] == "L":
            print("좌로 한번")
            way = (way - 1) % 4
        elif wayList[cntTime] == "D":
            print("우로 한번")
            way = (way + 1) % 4
    print(board)
    print(snake)
    print("---------")
