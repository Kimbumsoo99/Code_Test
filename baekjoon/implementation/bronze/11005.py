import sys
input = sys.stdin.readline

N, B = map(int, input().split())

tmp = {}
if B > 10:
    num = 10
    for i in range(65, 65 + B - 10):
        tmp[num] = chr(i)
        num += 1
result = ""
count = 0
while N > 0:
    tmp_num = N % B
    result = (str(tmp_num) if tmp_num < 10 else tmp[tmp_num]) + result
    N //= B
print(result)