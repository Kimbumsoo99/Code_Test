def solution(arr):
    answer = []
    print(len(answer))
    for i in arr:
        if len(answer) == 0 or answer[-1] != i:
            answer.append(i)
        else:
            continue

    return answer