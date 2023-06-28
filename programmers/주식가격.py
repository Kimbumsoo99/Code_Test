# #1 풀이
# queue를 사용해야한다 생각하고 풀었지만 너무 느리다는 문제점
from collections import deque
def solution(prices):
    answer = []
    down = deque()
    down_count = deque()
    price_len = len(prices)
    finish_index = set()

    for i in range(len(prices)):
        down.append(prices[i])
        down_count.append(price_len - 1 - i)
        # print(down, down_count)
        if i == price_len - 1:
            for j in range(price_len):
                answer.append(down_count.popleft())
            break

        for j in range(i):
            # print(i)
            # print(down, down_count)
            tmp = down.popleft()
            count = down_count.popleft()
            # print(tmp, count, prices[i])
            if j in finish_index or tmp <= prices[i]:
                down.append(tmp)
                down_count.append(count)
            elif tmp > prices[i]:
                down.append(tmp)
                down_count.append(i - j)  # 이 부분 고쳐야함
                finish_index.add(j)
        down.append(down.popleft())
        down_count.append(down_count.popleft())
        # print(down, down_count)
    return answer

# #2 풀이
# 위 풀이가 너무 느려 확인해보니 굳이 queue가 필요없는 문제였음.
# 그렇지만 N^2의 최악 시간복잡도에 경우 문제가 있음
def solution(prices):
    answer = []
    price_len = len(prices)
    down_count = [0] * price_len
    finish_index = set()

    for i in range(len(prices)):
        down_count[i] = price_len - 1 - i
        # print(down, down_count)
        if i == price_len - 1:
            answer = list(down_count)

        for j in range(i):
            # print(i)
            # print(down, down_count)
            # print(tmp, count, prices[i])
            if j in finish_index or prices[j] <= prices[i]:
                continue
            elif prices[j] > prices[i]:
                down_count[j] = i - j  # 이 부분 고쳐야함
                finish_index.add(j)
        # print(down, down_count)
    return answer

# #3 풀이
# 다른 사람 풀이를 보고 참고한 풀이이다.
# 전혀 생각못한 완전 탐색 풀이다.
# 충분히 다른 풀이도 존재할 것이라고 생각하지만 정말 좋은 방법인듯 하다.
def solution(prices):
    price_len = len(prices)
    answer = [0] * price_len
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, price_len):
            count += 1
            # print(prices[i], prices[j])
            if prices[i] > prices[j]:
                answer[i] = count
                break
            elif j == price_len - 1:
                answer[i] = count
    return answer

# #4 풀이
# 스택을 사용한 풀이
# 생각 충분히 할 수 있는 문제인데 왜 생각 못했지 싶음
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[i]:
            past, _ = stack.pop()
            answer[past] = i - past
        stack.append([i, prices[i]])

    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer