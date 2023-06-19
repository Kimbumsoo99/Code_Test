# S = 0
# S |= (1<<3)
# S |= (1<<1)
# S |= (1<<2)
# S |= (1<<3)
# print(S) # 1110
# S &= ~(1 << 3)
# print(S) # 0110
# S ^= (1 << 2)
# S ^= (1 << 4)
# print(S) # 10010
# S = 0              #비우기
# S = (1 << 21) - 1  #채우기

t = int(input())
for i in zip(*[input() for _ in range(t)]):
    # asdasd
    # qweqwe
    # asdads
    print(i)
    print(i[0], i[1])
    if t == 2:
        dict_tmp = dict(zip(i[0], i[1]))
        print(dict_tmp)
