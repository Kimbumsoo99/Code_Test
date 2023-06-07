import sys
input = sys.stdin.readline
N = int(input())

if N % 4 != 0:
    print("0")
elif N % 100 == 0 and N % 400 != 0:
    print("0")
else:
    print("1")