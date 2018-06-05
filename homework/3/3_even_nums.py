lst = input('print list of numbers (in format: 1,2,3): ').split(',')

i = 0
sum = 0

while i < len(lst):
    if i % 2 == 0:
        sum += int(lst[i])
    i += 1

multiply = sum * int(lst[len(lst) - 1])

print(multiply)