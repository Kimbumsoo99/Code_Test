import sys
input = sys.stdin.readline

sound = list(map(int, input().split()))

ascending = [1, 2, 3, 4, 5, 6, 7, 8]

if sound == ascending:
    print("ascending")
elif sound == sorted(ascending, reverse=True):
    print("descending")
else:
    print("mixed")