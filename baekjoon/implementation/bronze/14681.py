import sys

input = sys.stdin.readline

X = int(input())
Y = int(input())

if X > 0 and Y > 0:
    print("1")
elif X > 0:
    print("4")
elif Y > 0:
    print("2")
else:
    print("3")