import sys
input = sys.stdin.readline
N = int(input())
# numbers = input()
# word = []
# tmp = ""
# for i in numbers:
#     if i == " " or i == "\n":
#         word.append(int(tmp))
#         tmp = ""
#         continue
#     tmp += i

word = list(map(int, input().split()))
word.sort()
print(word[0], word[-1])
