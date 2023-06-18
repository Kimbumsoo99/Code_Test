import sys
input = sys.stdin.readline

words = []
count = 0
for i in range(5):
    words.append(input().strip())
    # print(words)
    # print(words[i])
    # print(len(words[i]))
    count += len(words[i])
# print(count)
i = 0
while True:
    for j in range(5):
        # print(words)
        # print(len(words[j]))
        # print(i)
        if len(words[j]) <= i:
            continue
        count -= 1
        print(words[j][i], end="")
        # print(words[j][i])
    if count == 0:
        exit(0)
    i += 1
    # print("\n")