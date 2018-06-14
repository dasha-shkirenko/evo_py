num = int(input(('Set number:' )))

if num > 10:
    print(num)
elif num < 5 and num > 0:
    num += 11
    if num > 13:
        print('number is bigger than 13')
    else:
        print(num)
else:
    num -= 100
    if num > -200 and num < -50:
        print('(-200; -50), number is {}'.format(num))
    else:
        print('something went wrong')





def count_symb(str, symbol):
    counter = 0
    i = 0

    for i in range(0, len(str)):
        if str[i] == symbol:
            counter += 1

    return counter


print(count_symb('Hello world', 'd'))