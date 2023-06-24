def solution(param):
    list_1 = param.split(".")
    print(list_1)
    for i in list_1:
        print(i)
    for i in range(4):
        print(list_1[i])

solution("192.168.0.1")