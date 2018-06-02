pwd = 1234
x = 0

while x < 5:
    password = int(input('print password'))

    if password != pwd:
        x += 1
        print('try again \nnumber of tries is {}'.format(5 - x))


    else:
        print("Win")
        x = 6


# num = 1
# secret_code = 9999
#
# while num <= 5:
#     password = int(input('print password'))
#     print('you used {} attempt out of 5'.format(num))
#
#     if password == secret_code:
#         print("Win")
#         num = 6
#
#     else:
#         num += 1
#         if num <= 5:
#             print('try again')