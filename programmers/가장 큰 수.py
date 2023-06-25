# 생각보다 많이 구현했음
# 그렇지만 제일 핵심을 못함
# 특정 예외 케이스들 몇개가 존재했는데
# 97, 978과 같은 경우나 3, 34, 30 같은 경우
# 이런 경우에 처리가 복잡했으나 str(n) * 3을 기준으로 sort를 했으면 가능했음.
# 해당 부분 알고리즘만 참고하고 나머지는 구현하였음.

def sort_num(numbers, current):
    numbers.sort(key=lambda x: str(x) * 3, reverse=True)
    # print(numbers)
    return numbers


def solution(numbers):
    answer = ''
    numbers.sort(key=lambda x: str(x)[0], reverse=True)
    # print(numbers)
    num_map = {}
    for i in numbers:
        c = str(i)[0]
        num_map[c] = num_map.get(c, 0) + 1
    # print(num_map)
    index, current = 0, 9
    while current > 0:
        end = (index + num_map[str(current)]) if str(current) in num_map else -1
        # print(current, end)
        if end == -1:
            current -= 1
            continue
        # print(numbers[index:end:])
        if num_map[str(current)] > 1:
            numbers[index:end:] = sort_num(numbers[index:end:], current)
        # print("여기", numbers)
        current -= 1
        index = end
    # print(numbers)
    for i in numbers:
        # print(i)
        answer += str(i)
    return str(int(answer))

# 그러나 코드가 너무 길어서 다른 코드도 좋아보임.

# 아래 코드는 좋은 코드
def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))