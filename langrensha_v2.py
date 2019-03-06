import random


def rn():
    renwu = ['狼人', '平民', '白狼', '女巫', '预言家', '平民']
    a = 5
    while a <= 1:
        rn = renwu[random.randint(0, a)]
        a = a - 1
        return rn


print(rn)
print(rn)
print(rn)
print(rn)

# if chuangjianrenwu():
