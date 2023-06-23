import sys
input = sys.stdin.readline

N, k = map(int, input().split())

x = list(map(int, input().split()))

# 삽입 정렬


# 선택 정렬
# 정렬이 됐던 말던 무조건 전체 리스트 순회
# 최선이든 최악이든 O(n^2)
# 구현
for i in range(N):
    for j in range(i+1, N):
        if x[i] < x[j]:
            x[i], x[j] = x[j], x[i]
print(x[k-1])


# 버블 정렬
# 거의 모든 상황에서 최악의 시간 복잡도
# 그렇지만 1번만 순회하는 이미 정렬된 자료에서는 최선의 성능
# 구현
# count = 0
# for i in range(N-1):
#     for j in range(N-1):
#         count += 1
#         if x[j] < x[j+1]:
#             x[j], x[j+1] = x[j+1], x[j]
# print(x)

