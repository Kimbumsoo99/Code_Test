import sys
input = sys.stdin.readline
# .rstrip() 는 오른쪽 공백을 전부 제거 해줌.
T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(A + B)
