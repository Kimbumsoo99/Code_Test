import sys

input = sys.stdin.readline

words = input().strip()

croatia = ["dz=", "c=", "s=", "z=", "lj", "nj", "d-", "c-"]
count = 0
while len(words) > 0:
    if words[0:3] == "dz=":
        words = words[3::]
        count += 1
    elif words[0:2] in croatia:
        words = words[2::]
        count += 1
    else:
        words = words[1::]
        count += 1
print(count)
