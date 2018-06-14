import random

# def loto_game(m):
#     win_n = set()
#     num_count = len(m)
#
#     if num_count > 100:
#         # 5 winning bubble
#         win_n = {randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60)}
#         return win_n.intersection(m)
#     elif num_count > 50:
#         # 4 winning bubble
#         win_n = {randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60)}
#         return win_n.intersection(m)
#     elif num_count > 20:
#         # 3 winning bubble
#         win_n = {randint(0, 60), randint(0, 60), randint(0, 60)}
#         return win_n.intersection(m)
#     elif num_count > 10:
#         # 2 winning bubble
#         win_n = {randint(0, 60), randint(0, 60)}
#         return win_n.intersection(m)
#     elif num_count > 1:
#         # 1 winning bubble
#         win_n = {randint(0, 60)}
#         (list(win_n.intersection(m))).sort()
#         return win_n
#     else:
#         return 'no arguments'
#
#
# print(loto_game([1, 2, 45, 45, 66, 3, 88,]))


# def loto(m, n):
# #     #  m - all bubbles
# #     #  n - winnings bubbles
# #     win_list =
# #
# #     if len(n) > len(m):
# #         print('too lot winning bubbles')
# #     else:
# #         for number in n:
# #             for i in m:
# #                 if number == i:
# #                     win_list.append(number)
# #
# #     return win_list
# #
# #
# # print(loto([1, 2, 45, 45, 66, 3, 88,], 3))



def lottery(num_win_bolls, total_bolls):
    result_list = []

    if num_win_bolls <= total_bolls:
        bolls = list(range(1, total_bolls + 1))
        for i in range(num_win_bolls):
            random.shuffle(bolls)
            result_list.append(bolls.pop())
        result_list.sort()
        return result_list
    else:
        return 'fail'


print(lottery(6, 100))