self_number = []
all_number = set()
not_self_number = set()


def notSelfNum(current_num):
    value = current_num
    while current_num > 0:
        value += current_num % 10
        current_num //= 10
    if value < 10001:
        return value
    else:
        return


for i in range(1, 10001):
    all_number.add(i)
    num = notSelfNum(i)
    not_self_number.add(num)

self_number = sorted(all_number - not_self_number)

for i in self_number:
    print(i)