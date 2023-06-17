import sys
input = sys.stdin.readline

N, M = map(int, input().split())

village = []
chicken_house = []
home = []
for i in range(N):
    village.append(list(map(int, input().split())))
    for j in range(len(village[i])):
        if village[i][j] == 2:
            chicken_house.append((i+1, j+1))
        elif village[i][j] == 1:
            home.append((i+1, j+1))

print(village)
print(chicken_house)
print(home)

chicken_comb = [0]*len(home)
temp = [chicken_comb[:] for i in range(len(chicken_house))]
print(temp)

history = [(0, 2500) for _ in range(len(home))]
for i in range(len(chicken_house)):
    for j in range(len(home)):
        r = abs(chicken_house[i][0] - home[j][0])
        c = abs(chicken_house[i][1] - home[j][1])
        if history[j][1] > r+c:
            history[j] = (i, r+c)

distance = 0
for i in history:
    distance += i[1]
print(distance)