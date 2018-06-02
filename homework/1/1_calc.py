a = int(input("Print a: "))
b = int(input("Print b: "))
operator = input("Print an operator: ")


if operator  not in ["+", "-", "**"]:
	print("operator if not defined")
elif operator == '+':
	output = a + b
	print(output)
elif operator == '-':
	output = a - b
	print(output)
elif operator == '**':
	output = a ** b
	print(output)
else:
	print("something went wrong")