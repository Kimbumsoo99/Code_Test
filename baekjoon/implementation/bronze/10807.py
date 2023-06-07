import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
collect = int(input())

count = 0
for i in nums:
    if collect == i:
        count += 1

print(count)