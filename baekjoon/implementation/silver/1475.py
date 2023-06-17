import sys

input = sys.stdin.readline

count = 1


def repeat_deck():
    return [0, 1, 2, 3, 4, 5, 7, 8, 9, 9]


N = list(map(int, input().rstrip()))
deck = repeat_deck()
for i in range(len(N)):
    if N[i] == 6:
        N[i] = 9
    if N[i] in deck:
        deck.pop(deck.index(N[i]))
    else:
        count += 1
        deck += repeat_deck()
        deck.pop(deck.index(N[i]))
print(count)
