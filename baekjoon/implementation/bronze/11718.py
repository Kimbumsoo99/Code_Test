while True:
    try:
        print(input())
    except:
        break

# input은 EOF를 받을 때 EOFError를 일으키지만
#
# sys.stdin.readline은 EOF를 받을 때 빈 문자열을 리턴합니다.