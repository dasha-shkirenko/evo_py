from random import randint

i = 0

while True:
    cub_1 = randint(1, 7)
    cub_2 = randint(1, 7)

    i += 1

    if cub_1 + cub_2 == 8:
        print("first cube: {}, second cube: {}, attempts: {}".format(cub_1, cub_2, i))
        break
    else:
        continue