import sys
input = sys.stdin.readline

N = int(input())

work = set()
for i in range(N):
    name, w = map(str, input().split())
    if w == "enter":
        work.add(name)
    else:
        work.remove(name)

for i in sorted(work, reverse=True):
    print(i)


