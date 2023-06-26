from collections import deque


def list_bigger(process, p_list):
    for i in p_list:
        if i > process:
            return False
    return True  # 현재 pop한게 가장 큰 값


def solution(priorities, location):
    answer = 1
    queue = deque(priorities)

    while len(queue) > 0:
        tmp = queue.popleft()
        is_exe = list_bigger(tmp, list(queue))
        if is_exe and location == 0:
            return answer
        elif is_exe:
            answer += 1
        else:
            queue.append(tmp)
        location -= 1
        if location < 0:
            location = len(queue) - 1

    return answer

