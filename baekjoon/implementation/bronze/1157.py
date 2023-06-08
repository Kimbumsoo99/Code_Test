import sys
# upper_str = str.upper()
# word = input().rstrip().upper()
input = sys.stdin.readline

word = input().rstrip()

big_a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z"]
small_a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
collect = {}

for i in word:
    if i in small_a:
        i = big_a[small_a.index(i)]
    if not (i in collect):
        collect[i] = 1
    else:
        collect[i] += 1
max_word = ""
max_count = 0

for i in collect.keys():
    if max_count < collect[i]:
        max_count = collect[i]
        max_word = i
    elif max_count == collect[i]:
        max_word = "?"

print(max_word)

# word = input()
#
# my_list = []    # list는 키워드이므로 사용을 피해주세요
# count_list = []
#
# def max_alphabet(word):
#     my_list = list(set(word.upper()))    # set으로 중복문자 없애기, 그리고 다시 리스트로 바꿔주기
#     for i in my_list:
#         count_list.append(word.upper().count(i))
#     if count_list.count(max(count_list)) >= 2:
#         return "?"
#     return my_list[count_list.index(max(count_list))]
#
# print(max_alphabet(word))