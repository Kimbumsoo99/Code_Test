while True:
    try:
        buffer = input()
        print(buffer)
    except:
        break
        
# sys.stdin.readline 은 EOF인 경우 ""를 리턴하기때문에, input으로 해야함