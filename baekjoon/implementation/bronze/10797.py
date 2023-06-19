import sys
input = sys.stdin.readline

T = int(input())

asc = list(map(int, input().split()))

count = 0
for i in asc:
    if i == T:
        count += 1

print(count)