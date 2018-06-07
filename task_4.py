# lst = input("Print numbers: ").split(',')
#
# def func_3(lst):
#     i = 0
#     count = 0
#
#     for i in range (0, len(lst)):
#         if int(lst[i]) >= 0:
#             count += 1
#
#     return count
#
# print(func_3(lst))

def lst_of_nums(lst):
    n = 0
    for i in lst:
        if i > 0:
            n += 1

    return  'count of positive items is {}'.format(n)

print(lst_of_nums([4, 5, 6, 9, -1, -4, -6]))