def arithmetic_arranger(problems, show_answers=True):
	for expression in problems:
		split = expression.split(" ")
		a = int(split[0])
		b = int(split[-1])
		operator = split[1]

		if operator == "+":
			result = a + b

		if operator == "-":
			result = a - b

		total_digits = max(len(list(str(a))), len(list(str(b))))

		divider = total_digits + 2
		divider = "-"*divider

		print(" " * 2 + str(a).rjust(total_digits))
		print(operator, str(b).rjust(total_digits))
		print(divider)
		if show_answers == True:
			print(str(result).rjust(total_digits + 2))


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')