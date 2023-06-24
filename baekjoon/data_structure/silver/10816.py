import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_dict = {}
for i in num_list:
    if not i in num_dict.keys():
        num_dict[i] = 1
    else:
        num_dict[i] += 1
M = int(input())
num_list2 = list(map(int, input().split()))
for i in num_list2:
    if i in num_dict.keys():
        print(num_dict[i], end=" ")
    else:
        print(0, end=" ")