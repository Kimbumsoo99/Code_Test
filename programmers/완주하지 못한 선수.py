def solution(participant, completion):
    answer = ''
    length_p = len(participant)
    length_c = len(completion)
    map_pc = {i: 0 for i in participant}
    for i in completion:
        map_pc[i] += 1
    for i in participant:
        map_pc[i] -= 1
        if map_pc[i] < 0:
            answer = i
            break

    return answer