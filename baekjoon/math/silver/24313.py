import sys

input = sys.stdin.readline

a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

func_fn = a1 * n + a0
func_fn2 = a1 * 100 + a0
func_gn = c * n

if func_fn <= func_gn and func_fn2 <= c * 100:
    print(1)
else:
    print(0)