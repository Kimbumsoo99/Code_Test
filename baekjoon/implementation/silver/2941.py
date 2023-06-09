import sys
input = sys.stdin.readline

words = "dz=z=dz="

croatia = ["dz=", "c=", "s=", "z=", "lj", "nj", "d-", "c-"]
index = {}
for i in croatia:
    if words.find(i):
        index[i] = words.find(i)


print(words)