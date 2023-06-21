array = [5, 4, 7, 3, 2, 8, 1, 6]

def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return

    pivot = start  # pivot은 첫 번째 원소
    left = start + 1
    right = end

    # 엇갈리기 전까지 반복
    while (left <= right):
        # pivot보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and array[left] <= array[pivot]):
            left += 1
            print(left, end)

        # pivot보다 작은 데이터를 찾을 때까지 반복
        while (right > start and array[right] >= array[pivot]):
            right -= 1

        # 엇갈렸다면 작은 데이터와 pivot을 스와핑
        if (left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 다시 퀵 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)