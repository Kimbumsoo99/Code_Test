import sys
input = sys.stdin.readline

N, M = map(int, input().split())

chess_board = []
for i in range(N):
    chess_board.append(input().rstrip())

WB_chess_board = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
BW_chess_board = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]

WB_count = 0
BW_count = 0
result = []

for start_i in range(N-8):
    for start_j in range(M-8):
        for i in range(start_i, start_i+8):
            for j in range(start_j, start_j+8):
                if chess_board[i][j] != WB_chess_board[i-start_i][j-start_j]:
                    WB_count += 1
                if chess_board[i][j] != BW_chess_board[i-start_i][j-start_j]:
                    BW_count += 1
        result.append(WB_count)
        result.append(BW_count)
        WB_count = 0
        BW_count = 0
print(result)
print(min(result))