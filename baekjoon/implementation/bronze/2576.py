sum = 0
min = 101
for i in range(7):
    num = int(input())
    if num % 2 == 1:
        if min > num:
            min = num
        sum += num
if min == 101:
    print(-1)
else:
    print(sum)
    print(min)