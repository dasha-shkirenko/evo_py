# lst = input("Print 3 numbers: ").split(',')
#
# def func_2(lst):
#     if int(lst[0]) == int(lst[1]) or int(lst[1]) == int(lst[2]) or int(lst[1]) == int(lst[2]):
#         return str("yes")
#
# print(func_2(lst))


def numbers(n1, n2, n3):
    if n1 == n2 or n2 == n3 or n1 == n3:
        return "yes"

print(numbers(3,5,5))