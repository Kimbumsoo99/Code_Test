def solution(name, yearning, photo):
    answer = []
    for i in photo:
        tmp = []
        for j in i:
            if j in name:
                tmp.append(yearning[name.index(j)])
        answer.append(sum(tmp))
    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))


# dict(zip(name, yearning))