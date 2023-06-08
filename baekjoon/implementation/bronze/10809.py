import sys
input = sys.stdin.readline

S = input().rstrip()
S_count = {}

for i in range(len(S)):
    if not (S[i] in S_count.keys()):
        S_count[S[i]] = i
    else:
        continue

for i in range(97, 123):
    if chr(i) in S_count.keys():
        print(str(S_count[chr(i)]), end=" ")
    else:
        print("-1", end=" ")