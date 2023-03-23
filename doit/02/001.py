# 백준 11720번
# 입력한 N개의 숫자를 모두 합해서 출력 하는 프로그램
# 입력으로 숫자의 개수와 공백 없이 주어진 N개의 숫자를 입력

# 순서
# n값 받기
# numbers 변수에 list 함수로 한 자리씩 나눠 받기
# sum 변수 선언 후 반복을 통해 numbers 변수값 더하기

n = input()
numbers = list(input())
sum = 0

for i in numbers:
    sum = sum+int(i)
print(sum)
