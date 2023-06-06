import sys
input = sys.stdin.readline
H, M = map(int, input().split())
timer = int(input())

H = H + (timer // 60)
M = M + (timer % 60)

if M >= 60:
    M -= 60
    H += 1
if H >= 24:
    H -= 24

print(H, M)