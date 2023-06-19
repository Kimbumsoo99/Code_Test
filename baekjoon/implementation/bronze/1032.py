import sys
input = sys.stdin.readline

N = int(input())

words = []
for i in range(N):
    s = input().rstrip()
    words.append(s)

result = words[0]
for i in range(1, N):
    for j in range(len(words[i])):
        if result[j] != words[i][j]:
            result = result[:j:] + "?" + result[j+1::]

print(result)
