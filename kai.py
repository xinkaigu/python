while 1 == 1:
    a = input()
    d = input()
    s = input()
    if d == '*':
        f = int(a) * int(s)
        print(int(f))
    elif d == '/':
        f = int(a) / int(s)
        print(int(f))
    elif d == '+':
        f = int(a) + int(s)
        print(int(f))
    elif d == '-':
        f = int(a) - int(s)
        print(int(f))
    else:
        print('程序不对')
