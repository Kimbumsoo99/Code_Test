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

# print(board)
# print(len(board),len(board[0]))

# 게임시작
while True:
    cntTime += 1
    # print("시간 ", cntTime)

    # 뱀 이동
    if way == 0:
        col += 1
    elif way == 1:
        row += 1
    elif way == 2:
        col -= 1
    elif way == 3:
        row -= 1

    # 게임 종료 조건
    if col > len(board[0]) - 1 or col < 1 or row > len(board) - 1 or row < 1:
        print(cntTime)
        # print("벽에 부딪혀 게임 종료")
        break
    if board[row][col] == 1:
        # print("몸 부딪")
        print(cntTime)
        break
    # print(board[row][col])

    if board[row][col] != 'A':
        # 사과가 없으면 한 칸 이동 후 제거
        board[row][col] = 1
        snake.appendleft([row, col])
        tail = snake.pop()
        board[tail[0]][tail[1]] = 0
    else:
        # 사과가 있으면 제거 하지 않음
        # print("🍅사과 발견 냠")
        board[row][col] = 1
        snake.appendleft([row, col])

    if cntTime in wayList.keys():
        if wayList[cntTime] == "L":
            # print("좌로 한번")
            way = (way - 1) % 4
        elif wayList[cntTime] == "D":
            # print("우로 한번")
            way = (way + 1) % 4
    # print(board)
    # print(snake)
    # print("---------")
