# 백준 1253번
# 주어진 N개의 수중 다른 두 수의 합으로 표현되는 개수 찾기

# 1 입력 수의 개수
# 2 입력 N개의 수의 값

# 정렬, 투 포인터 알고리즘
# 이런거 정하는 이유? 시간 복잡도 문제 때문

# 단, 정렬된 데이터에서 자기 자신을 좋은 수 만들기에 포함하면 안된다.

# 리스트 저장 후 정렬
# 투 포인터로 계산

N = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0
for k in range(N):
    find = A[k]
    i = 0
    j = N-1
    while i < j:
        if A[i] + A[j] == find:
            if i != k and j != k:
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:
            i += 1
        elif A[i] + A[j] > find:
            j -= 1

print(count)
