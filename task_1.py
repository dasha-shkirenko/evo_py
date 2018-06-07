num = int(input("Print number: "))

def func_0(num):
    if -10 < num < 10:
        num += 5
        return num
    else:
        num -= 10
        return num



print(func_0(num))