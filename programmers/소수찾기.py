# 시간초과 개 많이 났음. 41.7점 제일 긴거 Test 7 55.90ms
def solution(numbers):
    answer = 0
    # answer_list = []
    dict_num = {str(i): 0 for i in range(10)}
    for i in numbers:
        dict_num[i] += 1
    numbers = "".join(sorted(numbers, key=lambda x: int(x), reverse=True))

    is_good = 1
    for i in range(2, int(numbers) + 1):
        for j in range(2, i):
            if i % 2 == 0 or i % j == 0:
                is_good = -1
                break
        if is_good != -1:
            sosu.add(i)
        else:
            is_good = 1
        # print(sosu, i)
        if i in sosu:
            tmp = str(i)
            tmp_dict = dict_num.copy()
            for w in tmp:
                tmp_dict[w] -= 1
                if tmp_dict[w] < 0:
                    is_good = -1
                    break
            # print(tmp_dict, )
            if is_good == 1:
                answer += 1
                # answer_list.append(i)
            else:
                is_good = 1
    # print(answer_list)
    return answer

