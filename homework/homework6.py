def is_even_number(num):
	if num % 2 == 0:
		print(num, "is even.")
	else:
		print(num, "is odd.")


def compare(num1, num2):
	if num1 > num2:
		print(num1, "is greater than", num2)
	elif num1 == num2:
		print(num1, "and", num2, "are equal")
	else:
		print(num2, "is greater than", num1)


is_even_number(5)
is_even_number(4)
is_even_number(0)
is_even_number(-3)
is_even_number(-2)

compare(0, 0)
compare(1, 2)
compare(1, 1.01)
compare(3, 2)
compare(-2, -1)
compare(-2, -5)
