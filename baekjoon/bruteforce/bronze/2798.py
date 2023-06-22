import sys
input = sys.stdin.readline

N, M = map(int, input().split())
list_card = list(map(int, input().split()))

list_card = sorted(list_card, reverse=True)
result = 300000
a, b, c = 0, 0, 0
for i in range(len(list_card)):
    for j in range(i+1, len(list_card)):
        for k in range(j+1, len(list_card)):
            if M - (list_card[i] + list_card[j] + list_card[k]) < result and M >= (list_card[i] + list_card[j] + list_card[k]):
                result = M - (list_card[i] + list_card[j] + list_card[k])
                a, b, c = i, j, k
    if result == 0:
        break

print(list_card[a] + list_card[b] + list_card[c])