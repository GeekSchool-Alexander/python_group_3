sumator = 0
continue_flag = True
while continue_flag:
	inputed_number = int(input("Введите число: "))
	if inputed_number >= 0:
		sumator += inputed_number
		print("Текущее значение счетчика: ", sumator)
	else:
		continue_flag = False
print("Программа завершена.")
