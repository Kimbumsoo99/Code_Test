import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

x_w, y_h = abs(w - x), abs(h - y)

print(min(x, y, x_w, y_h))
