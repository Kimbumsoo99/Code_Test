import sys
input = sys.stdin.readline

N = int(input())

result = 1
count = 1
while True:
    if N == 1:
        break
    result += (6 * count)
    if result >= N:
        count += 1
        break
    count += 1
print(count)