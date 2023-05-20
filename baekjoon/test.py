from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
board = [[0 for j in range(N + 1)] for i in range(N + 1)]
# arr = [[0 for j in range(cols)] for i in range(rows)]

cntTime = 0

snake = deque()
way = 0
col, row = 1, 1
snake.appendleft([col, row])
# 게임시작
while (True):
    cntTime += 1

    if way == 0:
        col += 1
    elif way == 1:
        row += 1
    elif way == 2:
        col -= 1
    elif way == 3:
        row -= 1

    if col >= len(board[0])-1 or row >= len(board)-1:
        print("게임종료")
        break
    if board[col][row]=='A':
        snake.appendleft([col, row])
    else:
        snake.appendleft([col, row])
        snake.pop()
    #print(snake)
