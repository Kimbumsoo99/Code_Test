import sys

input = sys.stdin.readline

while True:
    numbers = input().strip()
    is_palin = True
    if numbers == "0":
        break
    for i in range(int(len(numbers) // 2)):
        if not numbers[i] == numbers[-i-1]:
            is_palin = False
    if is_palin:
        print("yes")
    else:
        print("no")