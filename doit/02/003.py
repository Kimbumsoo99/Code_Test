# 백준 11659번
# 합 배열 공식 S[i] = S[i-1]+A[i]

# 구간 합 공식 S[j] - S[i-1]  i에서 j까지 구간 합
# A[2]에서 A[5]까지의 구간합은 S[5] - S[1] 이다.

# 첫번째 줄 N의 수 입력, 합을 구해야하는 횟수 M 입력
# 두번째 줄 N개의 수
# 세번째 줄 M개의 줄에 합을 구해야 하는 구간 i와 j

import sys
input = sys.stdin.readline  # sys를 사용하는 이유는 반복문에서 input에 대한 시간초가 흐르기 때문
n, m = map(int, input().split())
num_list = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in num_list:
    temp = temp+i
    prefix_sum.append(temp)
print(prefix_sum)
for i in range(m):
    s, e = map(int, input().split())
    print(prefix_sum[e]-prefix_sum[s-1])
