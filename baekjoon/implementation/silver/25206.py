import sys
input = sys.stdin.readline

grade_score = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
sum_score = 0
avg_subject = 0
count_subject = 0
for i in range(20):
    subject, score, grade = map(str, input().split())
    if grade == "P":
        continue
    else:
        sum_score += float(score)
        count_subject += 1
        avg_subject += (float(score) * grade_score[grade])

print(avg_subject / sum_score)