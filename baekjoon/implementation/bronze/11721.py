import sys
input = sys.stdin.readline

words = input().strip()

while len(words) > 0:
    if len(words) > 10:
        print(words[:10])
        words = words[10::]
    else:
        print(words)
        words = ""