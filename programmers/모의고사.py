def people_answer(routine, an_len):
    return routine * (an_len // len(routine)) + routine[:an_len % len(routine)]


def solution(answers):
    answer = []
    an_len = len(answers)
    people = [0, 0, 0]
    routine_1 = [1, 2, 3, 4, 5]
    routine_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    routine_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    people[0] = people_answer(routine_1, an_len)
    people[1] = people_answer(routine_2, an_len)
    people[2] = people_answer(routine_3, an_len)
    print(people)

    p_dict = {i: 0 for i in range(3)}
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == people[j][i]:
                p_dict[j] += 1

    max_answer = max(p_dict.values())

    for i in p_dict:
        if p_dict[i] == max_answer:
            answer.append(i + 1)

    answer.sort()
    return answer