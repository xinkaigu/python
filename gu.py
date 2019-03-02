# lesson 15
#####################
def we(x):
    B = 0
    for mod in x:
        if B == 0:
            A = mod
            B = 0
        if A > mod:
            A = mod
            B = 1
        elif A < mod:
            B = 0
    return A


def get_max(x):
    b = 0
    for mod in x:
        if b < mod:
            b = mod
    return b


a = {2, 1, 3, 7, 5, 3, 9, 7, 8, }
w = we(a)
print(w)
#####################
# lesson 14
#####################
# def we(you, me):
#     for mod in you:
#         if mod == me:
#             return me
#
#     return 0
#
#
# a = {"A","B"}
# b = 'B'
# our = we(a, b)
# print(our)
#####################
# lesson 13
#####################
# def nihao(A, B, C):
#     return (A + B) * C
#
#
# a = nihao(1, 2, 3 )
# print(a)
# #####################
# lesson 12
#####################
# k = {1: "一年级", 2: "二年级", 3: "三年级", 4: "四年级", 5: "五年级", 6: "六年级"}
# while 1 == 1:
#     A = input()
#     try:
#         print(k[int(A)])
#     except:
#         print('你不是小学生')
#####################
# lesson 11
#####################
# 学校 = ["一年级", "二年级", "三年级", "四年级", "五年级", "六年级"]
# schoolen = len(学校)
# print(schoolen)
# while 1 == 1:
#     A = input()
#     try:
#         print(学校[int(A) - 1])
#     except:
#         print('你不是小学生')
#####################
# lesson 10
#####################

# while 1 == 1:
#     a = input()
#     d = input()
#     s = input()
#     if d == '*':
#         f = int(a) * int(s)
#         print(int(f))
#     elif d == '/':
#         f = int(a) / int(s)
#         print(int(f))
#     elif d == '+':
#         f = int(a) + int(s)
#         print(int(f))
#     elif d == '-':
#         f = int(a) - int(s)
#         print(int(f))
#     else:
#         print('程序不对')


#####################
# lesson 9
#####################
# import random
#
# print('开始练习')
# h=0
# while h < 9:
#     s = (random.randint(0, 10))
#     d = (random.randint(0, 10))
#     print('计算' + str(s) + '+' + str(d))
#     f = s + d
#     g = input()
#     if int(g) == f:
#         print('对了')
######################
# a = 1
# while 1 == 1:
#     a = a + 1
#     print(a)
#     if a == 6:
#         h=h+1
#     else:
#         print('错了')
#         h=0
#####################
# lesson 8
#####################
# # while True:
# #     a = input("搜索")
#     if a == '1':
#         print('一年级')
#     elif a == '2':
#         print("二年级")
#     elif a == '3':
#         print("三年级")
#     elif a == '4':
#         print("四年级")
#     elif a == '5':
#         print("五年级")
#     elif a == '6':
#         print("六年级")
#     else:
#         break
######################
# lesson 7
#         break
######################
# lesson 6
######################
# a = input("搜索")
# if a == '1':
#     print("一年级")
# elif a == '2':
#     print("二年级")
# elif a == '3':
#     print("三年级")
# elif a == '3':
#     print("四年级")
# elif a == '5':
#     print("五年级")
# elif a == '6':
#     print("六年级")
# else:
#     print("你不是小学生")
######################
# lesson 5
######################
# a = -1
# while a < 9:
#     a = a + 2
#     f = str(a)
#     print('同学 '+ f)
######################
# lesson 4
######################
# a = 0
# while a < 5:
#     a = a + 1
#     f = str(a)
#     print('同学 '+ f)
######################

# lesson 3
######################
# print('输入')
# a = input();
# print(a+'你好')
#######################
# lesson 2
#######################
# a=10
# if a >= 5:
#     print(9)
# elif a >= 9:
#     print(100)
# else:
#     print(10)
#######################


# lesson 1
#######################
# a = 11
# b = 100
# if a > 5:
#     print(a + b)
# else:
#     print(a * b)
#####################
