lst = input('print list of numbers (in format: 1,2,3): ').split(',')
num = int(input('print number: '))

i = 0

while i < len(lst):
    lst[i] = int(lst[i])
    i += 1


def to_degree(lst, num):
    if num < len(lst):
        print(lst[num]**num)
    else:
        print(-1)

to_degree(lst, num)