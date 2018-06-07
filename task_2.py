num = int(input("Print number: "))

def func_1(num):
    if -100 < num >= 100:
        num = 0
        return num
    else:
        return num + 1

print(func_1(num))