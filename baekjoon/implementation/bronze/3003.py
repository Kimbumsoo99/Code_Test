import sys
input = sys.stdin.readline

chess_list = [1, 1, 2, 2, 2, 8]

input_chess = list(map(int, input().split()))

change_list = [0 for i in range(6)]
for i in range(6):
    change_list[i] = 0 if input_chess[i] == chess_list[i] else chess_list[i] - input_chess[i]
    print(change_list[i], end=" ")
