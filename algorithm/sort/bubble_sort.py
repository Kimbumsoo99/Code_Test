bubble_x = list(map(int, input().split()))
N = len(bubble_x)
mode = int(input("(올림 1 내림 0)"))
count = 0

print(bubble_x)
for i in range(N):
    for j in range(N-1-i):
        if mode == 1 and bubble_x[j] < bubble_x[j+1]:
            count += 1
            bubble_x[j], bubble_x[j+1] = bubble_x[j+1], bubble_x[j]
        elif mode == 0 and bubble_x[j] > bubble_x[j+1]:
            count += 1
            bubble_x[j], bubble_x[j+1] = bubble_x[j+1], bubble_x[j]
print(bubble_x)
print(count)