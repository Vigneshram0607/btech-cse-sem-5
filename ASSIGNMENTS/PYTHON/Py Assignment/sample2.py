while True:
    try:
        a = input()
        print(a)
    except EOFError as a1:
        break