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

# while 1 == 1:
#     A = input('输入数字')
#     B = input('输入符号')
#     C = input('输入数字')
#     D = input('输入等于或符号')
#     if D == '=':
#         if B == '*':
#             Q = int(A) * int(C)
#             input(Q)
#         elif B == '/':
#             Q = int(A) / int(C)
#             print(Q)
#         elif B == '+':
#             Q = int(A) + int(C)
#             print(Q)
#         elif B == '-':
#             Q = int(A) - int(C)
#             print(Q)
#         else:
#             print('程序错误')
#     else:
#         E = input('输入数字')
#         if B == '*':
#             Q = int(A) * int(C)
#         elif B == '/':
#             Q = int(A) / int(C)
#         elif B == '+':
#             Q = int(A) + int(C)
#         elif B == '-':
#             Q = int(A) - int(C)
#         if D == '*':
#             W = int(Q) * int(E)
#             input(W)
#         elif D == '/':
#             W = int(Q) / int(E)
#             print(W)
#         elif D == '+':
#             W = int(Q) + int(E)
#             print(W)
#         elif D == '-':
#             W = int(Q) - int(E)
#             print(W)
#         else:
#             print('程序错误')
def hanshu(A, B, C, D, E):

    if D == '=':
        if B == '*':
            Q = int(A) * int(C)
            input(Q)

        elif B == '/':
            Q = int(A) / int(C)
            print(Q)
        elif B == '+':
            Q = int(A) + int(C)
            print(Q)
        elif B == '-':
            Q = int(A) - int(C)
            print(Q)
        else:
            print('程序错误')
    else:
        E = input('输入数字')
        if B == '*':
            Q = int(A) * int(C)
        elif B == '/':
            Q = int(A) / int(C)
        elif B == '+':
            Q = int(A) + int(C)
        elif B == '-':
            Q = int(A) - int(C)
        if D == '*':
            W = int(Q) * int(E)
            input(W)
        elif D == '/':
            W = int(Q) / int(E)
            print(W)
        elif D == '+':
            W = int(Q) + int(E)
            print(W)
        elif D == '-':
            W = int(Q) - int(E)
            print(W)
        else:
            print('E')


a = input('输入数字')
b = input('输入符号')
c = input('输入数字')
d = input('输入数字或符号')
hanshu(a, b, c, d, 'kong')
e = input('输入数字')
hanshu(a, b, c, d, e)
