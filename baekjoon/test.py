import sys
input = sys.stdin.readline

reg_data = list(map(str, input().split()))
print(reg_data)
reg_data[0] = reg_data[0].strip()
reg_data[1] = int(reg_data[1].strip())
print(reg_data)