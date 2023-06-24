# 정렬없이 중앙 값 구하기
def solutions(n):
    down_count = len(n) # 9
    up_count = 0 # 0
    answer_count = (len(n) - 1) // 2 # 4
    for i in range(len(n)):
        for j in range(0, i):
            if n[i] > n[j]:
                down_count -= 1
            else:
                up_count += 1
        for j in range(i+1,len(n)):
            if n[i] > n[j]:
                down_count -= 1
            else:
                up_count += 1
        if up_count == answer_count and down_count - 1 == answer_count:
            return n[i]
        else:
            down_count = len(n)
            up_count = 0


n = [1, 5, 32, 3, 68, 34, 99, 13, 24]
print(solutions(n))


