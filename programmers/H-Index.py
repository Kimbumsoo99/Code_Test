def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in citations:
        if i <= answer:
            break
        tmp = i
        answer += 1

    return answer