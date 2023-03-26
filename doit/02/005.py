# 백준 10986번 나머지합
# N개의 수를 주어졌을 때 연속된 부분의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램

# 첫 번째 입력 N과 M
# 두 번째 입력 연속된 숫자 N의 수

# (A + B) % C == ((A % C) + (B % C)) % C -> 나머지 연산하고 더하나 더하고 나머지 연산하나 같다.
# 구간합에서 i,j에 대한 구간합은 S[j] - S[i-1] 이다.
# 결국 S[i] % M 과 S[j] % M 이 같다면 (S[i]-S[j]) % M = 0

# 리스트 1 2 3 1 2 -> 합배열 1 3 6 7 9
# 합 배열 모든 값을 M(3) 으로 나눈 나머지 1 0 0 1 0

# sudo 코드 작성
# n 입력(수열의 개수)
# m 입력(나누어 떨어지는 수)
# A 입력(원본 수열)
# S 선언(합 배열)
# C 선언(같은 나머지의 인덱스 카운트)
# answer 선언

# for i -> 1 ~ n-1:
#   S[i] = S[i-1] + A[i] 합배열
# for i -> 0 ~ n-1:
#   S[i] % m을 한뒤 C 배열 증가 및 정답 1 증가
# for i -> 0 ~ m-1:
#   C[i]에서 2가지를 뽑는 경우의 수 정답에 더하기
# 결과 출력

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*n
C = [0]*m
S[0] = A[0]
answer = 0

for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        answer += 1
    C[remainder] += 1

for i in range(1, m):
    answer += (C[i] * (C[i]-1)//2)

print(answer)
