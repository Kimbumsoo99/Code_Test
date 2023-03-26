# 백준 2018번

# 어떠한 자연수 N은 연속된 자연수 합으로 나타낼 수 있다.
# 연속된 자연수의 합 가짓수를 알아내는 문제
# 15는 7+8, 4+5+6, 1+2+3+4+5 등

# 입력 자연수 N
# 출력 가짓수

# 투포인터 활용

import sys
input = sys.stdin.readline

n = int(input())
answer = 0

start_index = 1  # 투포인터 1p
end_index = 1  # 투포인터 2p
sum = 1

while end_index != n:
    if sum == n:
        answer += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(answer)
