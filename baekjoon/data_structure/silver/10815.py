import sys
input = sys.stdin.readline

N = int(input())

num_set = set(map(int, input().split()))

M = int(input())

num_list = list(map(int, input().split()))

for i in num_list:
    if i in num_set:
        print(1, end=" ")
    else:
        print(0, end=" ")