import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    bonus = 0
    score = 0
    quiz = input().strip()
    for j in quiz:
        if j == "O":
            score = score + bonus + 1
            bonus += 1
        else:
            bonus = 0
    print(score)
