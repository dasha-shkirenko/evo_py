# from random import randint
#
# def casino(num_1, num_2, num_3, rate):
#     win_num_1 = randint(0, 36)
#     win_num_2 = randint(0, 36)
#     win_num_3 = randint(0, 36)
#
#     one_num_win = 10
#     two_num_wins = 25
#     three_num_wins = 50
#
#     lst = [win_num_1, win_num_2, win_num_3]
#
#     if (
#             any(num == num_1 for num in lst) and
#             any(num == num_2 for num in lst) and
#             any(num == num_3 for num in lst)
#     ):
#         rate *= three_num_wins
#     elif (
#             any(num == num_1 for num in lst) and any(num == num_2 for num in lst) or
#             any(num == num_1 for num in lst) and any(num == num_3 for num in lst) or
#             any(num == num_2 for num in lst) and any(num == num_3 for num in lst)
#     ):
#         rate *= two_num_wins
#     elif (
#             any(num == num_1 for num in lst) or
#             any(num == num_2 for num in lst) or
#             any(num == num_3 for num in lst)
#     ):
#         rate *= one_num_win
#     else:
#         return 'You lose. Casino is an evil\n \nNumbers on roulette are {},{},{}\nYour numbers are {},{},{}'.format(
#             win_num_1, win_num_2, win_num_3, num_1, num_2, num_3
#         )
#
#
#     return 'Your winnings are {}$\n \nNumbers on roulette are {},{},{}\nYour numbers are {},{},{}'.format(
#             rate, win_num_1, win_num_2, win_num_3, num_1, num_2, num_3
#         )
#
# print(casino(1, 2, 3, 100))
#
#
#
#
#
from random import randint


def casino(num_1, num_2, num_3, rate):

    win_num_1 = randint(0, 36)
    win_num_2 = randint(0, 36)
    win_num_3 = randint(0, 36)

    one_num_win = 10
    two_num_wins = 25
    three_num_wins = 50

    user_nmb = [num_1, num_2, num_3]
    lst = [win_num_1, win_num_2, win_num_3]

    # a = [num for num in lst if num in user_nmb]
    a = []
    for num in lst:
        if num in user_nmb:
            a.append(num)
    if len(a) == 3:
        print('Your winnings are {}'.format(rate * three_num_wins))
    elif len(a) == 2:
        print('Your winnings are {}'.format(rate * two_num_wins))
    elif len(a) == 1:
        print('Your winnings are {}'.format(rate * one_num_win))
    print(a)


print(casino(1, 2, 3, 100))
