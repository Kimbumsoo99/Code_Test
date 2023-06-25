# 수학 구현 문제
# 조합과 관련된 풀이를 생각하였지만 결국 풀이 실패
# 다른 사람의 알고리즘을 보고 풀이를 만듬
# 그러나, 이 문제는 알고리즘 생각이 90%는 차지...

def solution(clothes):
    answer = 0
    hanger = {}
    for one in clothes:
        if one[1] in hanger:
            hanger[one[1]] += [one[0]]
        else:
            hanger[one[1]] = [one[0]]
    answer = 1
    for key in hanger.keys():
        # print(key, hanger[key])
        answer *= (len(hanger[key]) + 1)

    return answer - 1