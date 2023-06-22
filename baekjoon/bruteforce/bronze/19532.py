import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

# y = (c*d - a*f)//(b*d-a*e)
# x = (c*e-b*f)//(a*e-b*d)
#
# print(x, y)
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if c == a * x + b * y and f == d * x + e * y:
            print(x, y)