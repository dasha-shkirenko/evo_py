input = list(str(12345))
result = list('')

for i in range(1, len(input)+1):
	if i % 2 == 1:
		result.append(str(i))
	else:
		i = '0'
		result.append(i)

print(''.join(result))







