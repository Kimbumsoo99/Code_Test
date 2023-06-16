import sys
input = sys.stdin.readline

S = input().strip()

alphabet = {}
for i in range(97, 123):
    alphabet[chr(i)] = 0

for i in S:
    alphabet[i] += 1

for i in alphabet.keys():
    print(alphabet[i], end=" ")
