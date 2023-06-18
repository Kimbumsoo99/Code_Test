import sys
input = sys.stdin.readline

num_map = []
max_num = (-1, 0, 0)
for i in range(9):
    num_map.append(list(map(int, input().split())))
    for j in range(9):
        if max_num[0] < num_map[i][j]:
            max_num = (num_map[i][j], i+1, j+1)
print(max_num[0])
print(max_num[1], max_num[2])