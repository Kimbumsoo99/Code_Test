insert_x = list(map(int, input().split()))
N = len(insert_x)
mode = int(input("(올림 1 내림 0)"))
count = 0

print(insert_x)
for i in range(1, N):
    key = i
    while key > 0:
        if mode == 1 and insert_x[key] < insert_x[key-1]:
            count += 1
            insert_x[key], insert_x[key-1] = insert_x[key-1], insert_x[key]
            key -= 1
        elif mode == 0 and insert_x[key] > insert_x[key-1]:
            count += 1
            insert_x[key], insert_x[key-1] = insert_x[key-1], insert_x[key]
            key -= 1
        else:
            break
print(insert_x)
print(count)