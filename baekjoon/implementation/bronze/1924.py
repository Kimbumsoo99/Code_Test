import sys
input = sys.stdin.readline

month, day = map(int, input().split())

month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

result = 0
for i in range(1, month):
    result += month_day[i - 1]

result = (result + day - 1) % 7
if result == 0:
    print("MON")
elif result == 1:
    print("TUE")
elif result == 2:
    print("WED")
elif result == 3:
    print("THU")
elif result == 4:
    print("FRI")
elif result == 5:
    print("SAT")
else:
    print("SUN")
