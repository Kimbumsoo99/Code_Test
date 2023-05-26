'''
함수와 배열을 다루기(조건)
1. 배열에 포함된 문자열 비교하여 변환
2. 특정 조건에 대한 예외처리
3. 반복문 흐름 제어를 하며 종료 조건 적용
4. 다양한 테스트 케이스 예상 및 검증

내용
새로운 컴퓨터를 만든다. 8byte의 메모리 관리
BOOL 1byte
SHORT 2byte
FLOAT 4byte
INT 8byte
LONG 16byte

매개변수로 타입 입력한 것을 토대로
메모리 할당 결과를 8byte 단위로 끊어서 return

단, BOOL 타입 이후에 BOOL 타입은 바로 붙어서 할당할 수 있음.
뭐 BOOl, BOOL 이면 1,1 이 붙어서 하나의 2byte 11######
BOOL, SHORT를 하면 1,2가 중간에 3개로 구분 각각해서 하나의 1byte 1.11....
BOOL, FLOAT를 하면 1,4가 1...1111
BOOL, SHORT, FLOAT를 할당하기 위해서는 하나의 1byte에 1.111111
BOOL, INT면 1byte에 1......., 11111111
SHORT,BOOL 111.....
FLOAT, SHORT 111111..

타입이 하나라도 할당할 수 없으면 HALT RETURN
메모리 최대는 128byte임 즉, 16개가 최대임

입력 예시
INT, INT, BOOL, SHORT, LONG -> 11111111, 11111111, 1.11...., 11111111, 11111111
INT, SHORT, FLOAT, INT, BOOL -> 11111111, 11..1111, 11111111, 1.......
FLOAT, SHORT, BOOL, BOOL, BOOL, INT -> 11111111, 1......., 11111111
BOOL, LONG, SHORT, LONG, BOOL, LONG, BOOL, LONG, SHORT, LONG, LONG
-> 1......., 11111111, 11111111, 11......, 11111111, 1111111, 1......., 11111111,
11111111, 1......., 11111111,11111111, 11......, 11111111, 11111111 | 15byte 11111111, 11111111
-> HALT
'''


def solution(param):
    memory = [""]
    for _type in param:
        last = memory.pop()
        if _type == "LONG":
            if len(last) != 0:
                while len(last) < 8:
                    last += "."
                memory.append(last)
            memory.append("########")
            memory.append("########")
        elif _type == "INT":
            if len(last) != 0:
                while len(last) < 8:
                    last += "."
                memory.append(last)
            memory.append("########")
        elif _type == "FLOAT":
            if len(last) == 0:
                memory.append("####")
            elif len(last) == 8:
                memory.append(last)
                memory.append("####")
            elif len(last) < 8:
                while len(last) < 4:
                    last += "."
                last += "####"
                memory.append(last)
        elif _type == "SHORT":
            if len(last) == 0:
                memory.append("##")
            elif len(last) == 8:
                memory.append(last)
                memory.append("##")
            elif len(last) < 8:
                while len(last) < 2:
                    last += "."
                last += "##"
                memory.append(last)
        elif _type == "BOOL":
            if len(last) == 0:
                memory.append("#")
            elif len(last) == 8:
                memory.append(last)
                memory.append("#")
            elif len(last) < 8:
                last += "#"
                memory.append(last)

    if len(memory) > 16:
        return "HALT"
    last = memory.pop()
    while len(last) < 8:
        last += "."
    memory.append(last)

    result = ""
    for i in range(len(memory)):
        result += memory[i]
        if i != len(memory) - 1:
            result += ","
    return result


print(solution(["INT", "INT", "BOOL", "SHORT", "LONG"]))
print(solution(["INT", "SHORT", "FLOAT", "INT", "BOOL"]))
print(solution(["FLOAT", "SHORT", "BOOL", "BOOL", "BOOL", "INT"]))
print(solution(["BOOL", "LONG", "SHORT", "LONG", "BOOL", "LONG", "BOOL", "LONG", "SHORT", "LONG", "LONG"]))
