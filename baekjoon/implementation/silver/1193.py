import sys
input = sys.stdin.readline

# N = int(input())
#
# y, x = 1, 1
# turn = 0  # 0 오른쪽, 1 아래쪽
#
# while N > 1:
#     N -= 1
#     if turn == 0:
#         x += 1
#         turn = 1
#         tmp = x - 1
#         if N - tmp > 1:
#             x -= tmp
#             y += tmp
#             N -= tmp
#         else:
#             x -= (N - 1)
#             y += (N - 1)
#             break
#     else:
#         y += 1
#         turn = 0
#         tmp = y - 1
#         if N - tmp > 1:
#             x += tmp
#             y -= tmp
#             N -= tmp
#         else:
#             x += (N - 1)
#             y -= (N - 1)
#             break
#
# print(str(y) + "/" + str(x))

# ↑ 내가 짠 코드 / ↓ 더 짧은 코드

X = int(input())

line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line - X + 1
else:
    a = line - X + 1
    b = X

print(a, '/', b, sep='')