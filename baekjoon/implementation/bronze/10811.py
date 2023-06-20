import sys
input = sys.stdin.readline

N, M = map(int, input().split())

basket = [i+1 for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A, B = max(A, B) - 1, min(B, A) - 1
    basket[B:A+1] = list(reversed(basket[B:A+1:]))

for i in basket:
    print(i, end=" ")

# for _ in range(M):
#     i, j = map(int, input().split())
#     a[j:i-1:-1] = a[i:j+1]
# print(*a[1:])