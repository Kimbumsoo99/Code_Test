import sys
input = sys.stdin.readline

num_list = []
for i in range(5):
    num_list.append(int(input()))

print(int(sum(num_list) / len(num_list)))
print(sorted(num_list)[2])