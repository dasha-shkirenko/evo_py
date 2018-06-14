# def func(first_num, second_num, c = 3):
#     pass
#
#
# def func2(*args):
#     for i in args:
#         print(i)
#
# # func2(3, 5, 6, 55, 14, 2, 0)
#
#
#
# def func3(**kwards):
#     return kwards
#
# print(func3(c = 2, a = 3, v = 6))

def func(*args, **kwargs):
    return 'args = {} and kwards = {}'.format(args, kwargs)

print(func(1, 2, 3, a = 1, b = 2))