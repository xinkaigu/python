
import random

print('开始练习')
h=0
while h < 9:
    s = (random.randint(0, 10))
    d = (random.randint(0, 10))
    print('计算' + str(s) + '+' + str(d))
    f = s + d
    g = input()
    if int(g) == f:
        print('对了')
        h=h+1
    else:
        print('错了')
        h=0