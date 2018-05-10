str1 = input("Введите строку: ")
char_index = 0
for i in str1:
	print(i*(len(str1)-char_index))
	char_index += 1
