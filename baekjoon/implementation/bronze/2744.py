words = input()

for w in words:
    if ord(w) < 92:
        print(chr(ord(w) + 32),end="")
    else:
        print(chr(ord(w) - 32), end="")