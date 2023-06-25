# 장르 별로 가장 많이 재생된 노래 2개씩임
#
# 예외:
# 장르에 속한 곡이 하나라면 그 하나 선택
#
#
# 구현:
# 장르에 대하여 튜플 저장
# dict
# key: 장르, value: [(number, plays)]
#
# 각 장르에 길이를 봐서
# 2개 이하라면 그거 선택
# 2개초과면 선택폭이 달라짐
#
# 이때 각 장르에 plays를 모두 합쳐야함.
# 모두 합쳐서 가장 큰 장르에 대하여 key 순서 배열을 저장
#
# 이후 장르 내에서 많이 재생된 노래를 순서대로 출력(솔트하던가해서)

def solution(genres, plays):
    answer = []
    cd = {}
    for index, key in enumerate(zip(genres, plays)):
        cd[key[0]] = cd.get(key[0], []) + [(index, key[1])]
        # 위 아래 동일 코드, dict.get(key, non_key)로 값 가져오기
        # if key[0] in cd:
        #     cd[key[0]] += [(index, key[1])]
        # else:
        #     cd[key[0]] = [(index, key[1])]

    cd_play_sum = []
    for gen in cd.keys():
        sum_plays = 0
        for one in cd[gen]:
            sum_plays += one[1]
        cd_play_sum += [(gen, sum_plays)]
    cd_play_sum.sort(key=lambda x: x[1], reverse=True)
    # print(cd_play_sum)
    for k in cd_play_sum:
        print(cd[k[0]])
        cd[k[0]].sort(key=lambda x: x[1], reverse=True)
        if len(cd[k[0]]) <= 2:
            for i in range(len(cd[k[0]])):
                answer.append(cd[k[0]][i][0])
        else:
            for i in range(2):
                answer.append(cd[k[0]][i][0])
    print(answer)

    return answer

# 아쉬운 점. 파이썬 메소드가 너무 많음
# 파이썬에 의존적으로 풀었음
# 특히 람다 부분
