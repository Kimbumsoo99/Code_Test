x = list(map(int, input().split()))
select_x = x
insert_x = x
bubble_x = x
print(x)
# 18 23 15 32 29 38 40 50 69 20 30 50 100 39 20 4 77 81 86 88 50 99 3 43 92 52 64 10 30 68

N = int(len(x))
mode = int(input("(오름 1, 내림 0)"))
# 삽입 정렬
# 최선의 경우 전체 자료를 한번만 순회 O(n)
# 최악의 경우 O(n^2)
# 구현

# count = 0
# for i in range(1, N):
#     tmp = insert_x[i]
#     tmp_index = i
#     for j in range(i, -1, -1):
#         if tmp < insert_x[j]:
#             tmp = insert_x[j]
#             tmp_index = j
#         else:
#             break
#     insert_x[i], insert_x[tmp_index] = insert_x[tmp_index], insert_x[i]
#
# print("삽입", count)
# print(insert_x)
# print(select_x)


# 선택 정렬
# 정렬이 됐던 말던 무조건 전체 리스트 순회
# 최선이든 최악이든 O(n^2)
# 구현
count = 0
print(select_x)
for i in range(N):
    tmp = i
    print(select_x[tmp])
    for j in range(i+1, N):
        count += 1
        if mode == 1 and select_x[tmp] < select_x[j]:
            tmp = j
        elif mode == 0 and select_x[tmp] > select_x[j]:
            tmp = j
    select_x[i], select_x[tmp] = select_x[tmp], select_x[i]

print("선택", count)
print(select_x)


# 버블 정렬
# 거의 모든 상황에서 최악의 시간 복잡도
# 그렇지만 1번만 순회하는 이미 정렬된 자료에서는 최선의 성능
# 구현
count = 0
for i in range(N):
    for j in range(N-1):
        count += 1
        if mode == 1 and bubble_x[j] < bubble_x[j+1]:
            bubble_x[j], bubble_x[j+1] = bubble_x[j+1], bubble_x[j]
        elif mode == 0 and bubble_x[j] > bubble_x[j+1]:
            bubble_x[j], bubble_x[j+1] = bubble_x[j+1], bubble_x[j]
print("버블", count)
print(bubble_x)

