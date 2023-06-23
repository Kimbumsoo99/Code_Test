select_x = list(map(int, input().split()))
N = len(select_x)
mode = int(input())
count = 0

print(select_x)
for i in range(N):
    tmp = i
    print(select_x[tmp])
    for j in range(i+1, N):
        count += 1
        if mode == 1 and select_x[tmp] < select_x[j]:
            tmp = j
        elif mode == 0 and select_x[tmp] > select_x[j]:
            tmp = j
    select_x[i], select_x[tmp] = select_x[tmp], select_x[i]
print(select_x)