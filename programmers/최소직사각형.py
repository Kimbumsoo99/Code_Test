def solution(sizes):
    answer = 0
    x = 0
    y = 0
    for i in sizes:
        tmp_x, tmp_y = max(i[0], i[1]), min(i[0], i[1])
        if x < tmp_x:
            x = tmp_x
        if y < tmp_y:
            y = tmp_y
    answer = x * y
    return answer