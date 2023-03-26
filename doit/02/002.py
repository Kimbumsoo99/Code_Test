# 백준 1546번 단순 연산 평균
# 자기 점수 / 최대 점수 * 100
# 이 방법을 통해 새로운 평균을 구하는 프로그램

# 입력
# 과목의 개수 N, 성적

# 점수가 A,B,C인 경우 (A / M * 100 + B / M * 100 + C / M * 100) / 3 = (A + B + C) / 3M * 100

# n에 과목 수 입력
# mylist에 점수 정보 저장
# mymax에 점수 중 가장 큰 수 저장
# sum에 위 계산대로  데이터 값 구해서 출력

n = input()
mylist = list(map(int, input().split()))
print(mylist)
mymax = max(mylist)
sum = sum(mylist) / mymax / 3 * 100

print(sum)
