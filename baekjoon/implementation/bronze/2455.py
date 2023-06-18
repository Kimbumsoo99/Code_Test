import sys
input = sys.stdin.readline

train_people = 0
result = 0
for i in range(4):
    out_people, in_people = map(int, input().split())
    train_people -= out_people
    train_people += in_people
    if result < train_people:
        result = train_people
print(result)