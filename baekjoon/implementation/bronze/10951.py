import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
    except Exception as e:
        # print(e)
        # exit(e)
        break
