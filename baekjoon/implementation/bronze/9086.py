import sys
input = sys.stdin.readline

T = int(input())

string = []
for i in range(T):
    string.append(input())

for i in range(T):
    print(string[i][0] + string[i][-2])