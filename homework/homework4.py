inp = input('Введите температуру: ')
if len(inp):
	t = int(inp)
	if (t < -30) or (t > 30):
		print("Не выходи из дома!")
	elif -30 <= t and t < -10:
		print('Надень пуховик')
	elif -10 <= t  and t < 5:
		print('Надень пальто')
	elif 5 <= t and t < 15:
		print('Надень кофту')
	elif 15 <= t and t <= 30:
		print('Надень футболку')
else:
	print("ОШИБКА! Пустой ввод.")
