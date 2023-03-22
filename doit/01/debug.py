# 오류가 있는 코드 4가지
# 배열의 주어진 범위의 합을 2로 나눈 몫을 구하시오.
# 아래 코드보다 실제 코딩테스트 코드가 훨씬 길기 때문에 눈으로 찾더라도 디버깅 연습하기


import random

testcase = int(input())

A = [0]*(100001)

for i in range(0, 100001):
    A[i] = random.randrange(1, 101)

for t in range(1, testcase+1):
    answer = 0
    start, end = map(int, input().split())

    for i in range(start, end+1):
        answer = answer+A[i]

    print(str(t)+" "+str(answer//2))
