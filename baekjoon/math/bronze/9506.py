import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == -1:
        break
    num_arr = []
    for i in range(1, int(N/2) + 1):
        if N % i == 0:
            num_arr.append(i)
    if sum(num_arr) == N:
        print(N, end=" ")
        print("= ", end="")
        for j in num_arr:
            if j == num_arr[-1]:
                print(j)
            else:
                print(j, end=" + ")
    else:
        print(N, end=" ")
        print("is NOT perfect.")