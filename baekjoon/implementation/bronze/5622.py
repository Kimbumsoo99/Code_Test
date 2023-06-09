import sys
input = sys.stdin.readline

second = 0
words = input().strip()

for i in words:
    second += 2
    if ord(i) < ord('D'):
        second += 1
    elif ord(i) < ord('G'):
        second += 2
    elif ord(i) < ord('J'):
        second += 3
    elif ord(i) < ord('M'):
        second += 4
    elif ord(i) < ord('P'):
        second += 5
    elif ord(i) < ord('T'):
        second += 6
    elif ord(i) < ord('W'):
        second += 7
    else:
        second += 8
print(second)

