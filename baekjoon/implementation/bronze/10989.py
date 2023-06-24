import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(input()))

num_list.sort()
# 버블 - 메모리 초과
# for i in range(N):
#     for j in range(N-1-i):
#         if num_list[j] > num_list[j+1]:
#             num_list[j], num_list[j+1] = num_list[j+1], num_list[j]


# 삽입 - 메모리 초과
# for i in range(1, N):
#     key = i
#     while key > 0:
#         if num_list[key] < num_list[key-1]:
#             num_list[key], num_list[key-1] = num_list[key-1], num_list[key]
#             key -= 1
#         else:
#             break

# 선택 - 메모리 초과
# for i in range(N):
#     tmp = i
#     for j in range(i+1, N):
#         if num_list[tmp] > num_list[j]:
#             tmp = j
#     num_list[i], num_list[tmp] = num_list[tmp], num_list[i]

for i in range(N):
    print(num_list[i])