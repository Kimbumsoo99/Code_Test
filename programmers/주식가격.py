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