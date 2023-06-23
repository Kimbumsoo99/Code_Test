select_x = list(map(int, input().split()))
N = len(select_x)
mode = int(input("(올림 1 내림 0)"))
count = 0

print(select_x)
for i in range(N):
    tmp = i
    for j in range(i+1, N):
        if mode == 1 and select_x[tmp] < select_x[j]:
            count += 1
            tmp = j
        elif mode == 0 and select_x[tmp] > select_x[j]:
            count += 1
            tmp = j
    select_x[i], select_x[tmp] = select_x[tmp], select_x[i]
print(select_x)
print(count)