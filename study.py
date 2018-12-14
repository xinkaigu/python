import random

while 1 == 1:
    a = (random.randint(1, 7))
    if a == 1:
        a = (random.randint(1, 7))
    elif a == 2:
        a = (random.randint(1, 7))
    elif a == 3:
        a = (random.randint(1, 7))
    b = (random.randint(1, 7))
    if b == 1:
        b = (random.randint(1, 7))
    elif b == 2:
        b = (random.randint(1, 7))
    elif b == 3:
        b = (random.randint(1, 7))
    c = (random.randint(1, 7))
    if c == 1:
        c = (random.randint(1, 7))
    elif c == 2:
        c = (random.randint(1, 7))
    elif c == 3:
        c = (random.randint(1, 7))
    d = (random.randint(1, 7))
    if d == 1:
        d = (random.randint(1, 7))
    elif d == 2:
        d = (random.randint(1, 7))
    elif d == 3:
        d = (random.randint(1, 7))
    e = (random.randint(1, 7))
    if e == 1:
        e = (random.randint(1, 7))
    elif e == 2:
        e = (random.randint(1, 7))
    elif e == 3:
        e = (random.randint(1, 7))
    f = (random.randint(1, 7))
    if f == 1:
        f = (random.randint(1, 7))
    elif f == 2:
        f = (random.randint(1, 7))
    elif f == 3:
        f = (random.randint(1, 7))
    g = (random.randint(1, 7))
    if g == 1:
        g = (random.randint(1, 7))
    elif g == 2:
        g = (random.randint(1, 7))
    elif g == 3:
        g = (random.randint(1, 7))
    if a == 1:
        print('首领')
        input()
        qw = 1
    elif a == 2:
        print('女巫')
        input()
        qw = 2
    elif a == 3:
        print('预言家')
        input()
        qw = 1
    elif a == 4:
        print('狼人')
        input()
        qw = 1
    elif a == 5:
        print('平民')
        input()
        qw = 1
    elif a == 6:
        print('猎人')
        input()
        qw = 1

    else:
        print('白痴')
        input()
        qw = 100
    if b == 1:
        print('首领')
        input()
        we = 1
    elif b == 2:
        print('女巫')
        input()
        we = 2
    elif b == 3:
        print('预言家')
        input()
        we = 1
    elif b == 4:
        print('狼人')
        input()
        we = 1
    elif b == 5:
        print('平民')
        input()
        we = 1
    elif b == 6:
        print('猎人')
        input()
        we = 1
    else:
        print('白痴')
        input()
        we = 100
    if c == 1:
        print('首领')
        input()
        er = 1
    elif c == 2:
        print('女巫')
        input()
        er = 2
    elif c == 3:
        print('预言家')
        input()
        er = 1
    elif c == 4:
        print('狼人')
        input()
        er = 1
    elif c == 5:
        print('平民')
        input()
        er = 1
    elif c == 6:
        print('猎人')
        input()
        er = 1
    else:
        print('白痴')
        input()
        er = 100
    if d == 1:
        print('首领')
        input()
        rt = 2
    elif d == 2:
        print('女巫')
        input()
        rt = 1
    elif d == 3:
        print('预言家')
        input()
        rt = 1
    elif d == 4:
        print('狼人')
        input()
        rt = 1
    elif d == 5:
        print('平民')
        input()
        rt = 1
    elif d == 6:
        print('猎人')
        input()
        rt = 1
    else:
        print('白痴')
        input()
        rt = 100
    if e == 1:
        print('首领')
        input()
        ty = 1
    elif e == 2:
        print('女巫')
        input()
        ty = 2
    elif e == 3:
        print('预言家')
        input()
        ty = 1
    elif e == 4:
        print('狼人')
        input()
        ty = 1
    elif e == 5:
        print('平民')
        input()
        ty = 1
    elif e == 6:
        print('猎人')
        input()
        ty = 1
    else:
        print('白痴')
        input()
        ty = 100
    if f == 1:
        print('首领')
        input()
        yu = 1
    elif f == 2:
        print('女巫')
        input()
        yu = 2
    elif f == 3:
        print('预言家')
        input()
        yu = 1
    elif f == 4:
        print('狼人')
        input()
        yu = 1
    elif f == 5:
        print('平民')
        input()
        yu = 1
    elif f == 6:
        print('猎人')
        input()
        yu = 1
    else:
        print('白痴')
        input()
        yu = 100
    if g == 1:
        print('首领')
        input()
        ui = 1
    elif g == 2:
        print('女巫')
        input()
        ui = 2
    elif g == 3:
        print('预言家')
        input()
        ui = 1
    elif g == 4:
        print('狼人')
        input()
        ui = 1
    elif g == 5:
        print('平民')
        input()
        ui = 1
    elif g == 6:
        print('猎人')
        input()
        ui = 1
    else:
        print('白痴')
        input()
        ui = 100
    print('天黑请闭眼')
    input()
    print('狼人请睁眼')
    input()
    print('请选择你们要杀的人')
    input()
    o = input('选吧')
    if o == '1':
        qw = qw - 1
    elif o == '2':
        we = we - 1
    elif o == '3':
        er = er - 1
    elif o == '4':
        rt = rt - 1
    elif o == '5':
        ty = ty - 1
    elif o == '6':
        yu = yu - 1
    elif o == '2':
        ui = ui - 1
    print('狼人请闭眼')
    input()
    print('女巫请睁眼')
    input()
    print('今晚被杀的人是' + str(o) + '号')
    input()
    print('你要使用毒药或解药')
    input()
    qwe = input('毒药或解药')
    input()
    if qwe == '解药':
        if o == '1':
            qw = qw + 1
        elif o == '2':
            we = we + 1
        elif o == '3':
            er = er + 1
        elif o == '4':
            rt = rt + 1
        elif o == '5':
            ty = ty + 1
        elif o == '6':
            yu = yu + 1
        elif o == '2':
            ui = ui + 1
    else:
        input()
        wer = input('你要杀谁')
        if o == '1':
            qw = qw - 1
        elif o == '2':
            we = we - 1
        elif o == '3':
            er = er - 1
        elif o == '4':
            rt = rt - 1
        elif o == '5':
            ty = ty - 1
        elif o == '6':
            yu = yu - 1
        elif o == '2':
            ui = ui - 1
    print('女巫请闭眼')
