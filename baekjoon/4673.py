N = 10000

def isNum(i, num):
    result = i
    while i > 0:
        tmp = i % 10
        i = i // 10
        result += tmp
    if num == result:
        return True
    else:
        return False


for num in range(1, N + 1):
    check = True
    for i in range(num - 1, 0, -1):
        if isNum(i, num):
            check = False
            break
    if check:
        print(num)
