# Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
# затем перемножить эту сумму и последний элемент исходного массива.
# Не забудьте, что первый элемент массива имеет индекс 0.
# Для пустого массива результат всегда 0 (ноль).
# Входные данные: Список (list) целых чисел (int).
# Выходные данные: Число как целочисленное (int)

lst = input('print list of numbers (in format: 1,2,3): ').split(',')

i = 0
sum = 0

while i < len(lst):
    if i % 2 == 0:
        sum += int(lst[i])
    i += 1

multiply = sum * int(lst[len(lst) - 1])

print(multiply)