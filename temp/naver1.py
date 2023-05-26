'''
함수 구현문제 (조건)
1. 함수 선언해야함.
2. 함수 내부에서 배열 탐색
3. 배열 앞뒤 값 비교 후 중복되는 횟수 카운트하며 변경
4. 배열과 다른 타입 Set, Map 등을 활용하여 비교

문항
자연수 들은 arr이 매개변수로 주어짐.
배열 안의 숫자들 중 앞 -> 뒤 순서로 중복되는 숫자 횟수를 계산해서 배열로 return하는 함수
중복되는 수 없다면 배열에 -1을 채워서 return
'''


def solution(arr):
    arr_map = {}
    count = []
    for i in arr:
        if i in arr_map:
            arr_map[i] += 1
        else:
            arr_map[i] = 1
    for key in sorted(arr_map.keys()):
        if arr_map[key] > 1:
            count.append(arr_map[key])
    if len(count) == 0:
        count.append(-1)
    return count


arr1 = [4, 4, 23, 94, 30, 20, 49, 50, 4, 4, 2, 2, 2, 2, 2, 2, 94, 94, 30, 30, 20, 1, 1]
arr2 = [3, 2, 4, 4, 2, 5, 2, 5, 5]
arr3 = [3, 5, 7, 9, 1]

print(solution(arr1))
print(solution(arr2))
print(solution(arr3))
