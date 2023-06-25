from collections import deque
def solution(progresses, speeds):
    answer = []
    queue = deque()
    for index, value in enumerate(zip(progresses, speeds)):
        day = (100 - value[0]) // value[1]
        if (100 - value[0]) % value[1] != 0:
            day += 1
        queue.appendleft(day)
    print(queue)
    tmp = -1
    count = 0
    while len(queue) > 0:
        count += 1
        if tmp == -1:
            tmp = queue.pop()
            # print(tmp, count, queue)
        else:
            # print(tmp, count, queue, queue[-1])
            if queue[-1] <= tmp:
                queue.pop()
            else:
                tmp = -1
                answer.append(count-1)
                count = 0
    answer.append(count)
    return answer