# 정렬 알고리즘 사용
# 없으면 구현하면 그만이지만, N^2 정렬만 구현 가능
# NlogN 구현 방식을 배워야 할 필요성이 있음

def solution(array, commands):
    answer = []
    for command in commands:
        tmp = array[command[0]-1:command[1]:]
        tmp.sort()
        # print(tmp)
        answer.append(tmp[command[2]-1])
    return answer