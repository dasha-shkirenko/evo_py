tpl = tuple(input('print list of numbers (in format: 1,2,3): ').split(','))

def tuple_sort(tpl):
    lst = []
    i = 0

    for i in range(0, len(tpl)):
        lst.append(int(tpl[i]))

    lst.sort(key=abs)
    print(lst)

tuple_sort(tpl)

