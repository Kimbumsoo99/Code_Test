words = input()
ok = 1
for i in range(len(words) // 2):
    if words[i] == words[-i - 1]:
        continue
    else:
        ok = 0
        break
print(ok)