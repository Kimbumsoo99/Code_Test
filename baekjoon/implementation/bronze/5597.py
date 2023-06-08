import sys

input = sys.stdin.readline

# students = []
students = set(_ for _ in range(1, 31))

for i in range(28):
    students.remove(int(input()))

students = sorted(students)
for i in students:
    print(i)
#
# for i in range(1, 31):
#     if not (i in students):
#         print(i)


# set이 더 좋은 풀이과정 이었음