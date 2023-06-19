N = input().rstrip()
N = N[len(N):0:-1] + N[0]
result = 0
for i in range(len(N)):
    num = 0
    if N[i] == 'A':
        num = 10
    elif N[i] == 'B':
        num = 11
    elif N[i] == 'C':
        num = 12
    elif N[i] == 'D':
        num = 13
    elif N[i] == 'E':
        num = 14
    elif N[i] == 'F':
        num = 15
    else:
        num = int(N[i])
    tmp = 1
    for j in range(i):
        tmp *= 16
    result += tmp * num
print(result)

# 아래도 정답
# print(int(input(), 16))