# 1회차 효율성에서 탈락
def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        tmp = phone_book[i]
        tmp_len = len(tmp)
        for j in range(0, i):
            if phone_book[j][:tmp_len:] == tmp:
                answer = False
                return answer
        for j in range(i + 1, len(phone_book)):
            if phone_book[j][:tmp_len:] == tmp:
                answer = False
                return answer

    return answer

# 2회차 정렬 사용
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        tmp = phone_book[i]
        tmp_len = len(tmp)
        if phone_book[i+1][:tmp_len:] == tmp:
            answer = False
            return answer
    return answer

# 3회차 해시테이블 사용 (제일 정석, 다른 사람 풀이 참고)
def solution(phone_book):
    answer = True
    phone_set = set(phone_book)

    for i in phone_book:
        tmp = ""
        for j in i:
            tmp += j
            if tmp in phone_set and tmp != i:
                answer = False
    return answer