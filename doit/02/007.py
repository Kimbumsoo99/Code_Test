# 백준 1940번

# 1 입력 재료의 개수
# 2 입력 갑옷이 완성되는 번호의 합
# 3 재료들

# 재료들의 합을 통해 만들어지는 갑옷에 수를 나타내어라.

# 투 포인터

# 리스트 저장 배열 오름차순 정렬
# 투포인터를 양쪽 끝에 위치시킨 후 적합한 포인터 이동 원칙 활용
# 이동원칙
# A[i] + A[j] > M: j--; 번호의 합이 M보다 크면 큰 번호 index 감소
# A[i] + A[j] < M: i--; 번호의 합이 M보다 작으면 작은 번호 index 증가
# A[i] + A[j] == M: i++; j--; count++; 양쪽 포인터 모두 이동 후 count 증가

import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
A = list(map(int, input().split()))
A.sort()  # 위 list에서 한 번에 처리 X
i, j = 0, len(A)-1
count = 0

while i < j:
    if A[i]+A[j] > m:
        j -= 1
    elif A[i]+A[j] < m:
        i += 1
    elif A[i]+A[j] == m:
        i += 1
        j -= 1
        count += 1

print(count)
