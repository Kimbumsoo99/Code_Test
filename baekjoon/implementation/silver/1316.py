import sys
input = sys.stdin.readline

N = int(input())

count = 0
last = ""
duple = []
for i in range(N):
    words = input().rstrip()
    tmp = 1
    for index, word in enumerate(words):
        if index == 0:
            last = word
            duple.append(word)
            continue
        elif last == word:
            continue
        else:
            last = word
            if word in duple:
                tmp = 0
                break
            duple.append(word)
    duple = []
    last = ""
    count += tmp

print(count)



