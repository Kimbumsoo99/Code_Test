def solution(id_list, report, k):
    answer = [0] * len(id_list)
    black_list = {}
    push_id = {}

    for i in id_list:
        black_list[i] = 0
        push_id[i] = [0]
    # print(black_list)
    # print(push_id)

    report = list(set(report))
    # print(report)
    for i in report:
        _id, report_id = i.split()
        # print(i)
        black_list[report_id] += 1
        push_id[_id].append(report_id)
        if black_list[report_id] >= k:
            for j in id_list:
                if report_id in push_id[j]:
                    push_id[j][0] += 1
        # print(push_id, black_list)
    for i in black_list.keys():
        if black_list[i] >= k:
            for j in push_id.keys():
                if i in push_id[j]:
                    push_id[j][0] += 1

    for i in range(len(id_list)):
        answer[i] = push_id[id_list[i]][0]

    return answer