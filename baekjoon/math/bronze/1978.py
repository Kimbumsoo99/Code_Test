import sys
input = sys.stdin.readline

N = int(input())

num_arr = list(map(int, input().split()))


tmp = [2, 3]
for i in range(2, max(num_arr) + 1):
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            break
        elif j == int(i / 2):
            tmp.append(i)
count = 0
for i in num_arr:
    if i == 1:
        continue
    elif i in tmp:
        count += 1
print(count)
