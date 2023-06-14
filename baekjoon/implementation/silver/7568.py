import sys
input = sys.stdin.readline

N = int(input())

people_list = {}

for i in range(N):
    x, y = map(int, input().split())
    people_list[i] = [x, y, 1]  # 몸무게, 키, 등수

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            if people_list[i][0] < people_list[j][0] and people_list[i][1] < people_list[j][1]:
                people_list[i][2] += 1

for i in range(N):
    print(people_list[i][2], end=" ")