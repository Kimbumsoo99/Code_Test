import sys
input = sys.stdin.readline

N = input().rstrip()

good = N
count = 0

if int(N) < 10:
    N = str("0" + N[0])
    good = N

while True:
    count += 1
    tmp = int(N[0]) + int(N[1])
    if tmp < 10:
        tmp = N[1] + str(tmp)[0]
    else:
        tmp = N[1] + str(tmp)[1]
    N = str(tmp)
    if good == N:
        break
print(count)