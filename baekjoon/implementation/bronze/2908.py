import sys

input = sys.stdin.readline

A, B = map(str, input().split())

# A = "".join(reversed(A))
# reversed_A = A[::-1]
reverse_A = ""
reverse_B = B[::-1]
for i in range(len(A)):
    reverse_A += A[-i - 1]

if int(reverse_B) > int(reverse_A):
    print(reverse_B)
else:
    print(reverse_A)