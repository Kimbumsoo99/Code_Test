import sys
input = sys.stdin.readline

N, B = map(str, input().split())

tmp = {}
if int(B) > 10:
    num = 10
    for i in range(65, 65+int(B)-10):
        tmp[chr(i)] = num
        num += 1

m = len(N) - 1
result = 0
for i in N:
    result += int(i) * (int(B) ** m) if i not in tmp.keys() else tmp[i] * (int(B) ** m)
    m -= 1
print(result)