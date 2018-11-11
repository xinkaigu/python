import random

print('开始练习')
h = 0
j = 0
while h < 51:
    s = (random.randint(0, 10))
    d = (random.randint(0, 10))
    print('计算' + str(s) + '+' + str(d))
    f = s + d
    g = input()
    if int(g) == f:
        print('对了')
        h = h + 1
        j = j + 1
        print('您已做' + str(j) + '道题')
    else:
        print('错了')
        h = 0
        j = 0
        print('您已做' + str(j) + '道题')
