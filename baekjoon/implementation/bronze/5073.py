import sys
input = sys.stdin.readline

while True:
    A, B, C = map(int, input().split())
    tmp = sorted([A, B, C], reverse=True)
    if A == B == C == 0:
        break
    elif A == B == C:
        print("Equilateral")
    elif tmp[1] + tmp[2] <= tmp[0]:
        print("Invalid")
    elif A != B and B != C and A != C:
        print("Scalene")
    else:
        print("Isosceles")