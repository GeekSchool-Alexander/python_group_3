# Создать два разных списка с числами.
list_one = [1,2,3]
list_two = [5,6,7,8]
# Присвоить любому элементу первого списка значение элемента второго списка.
list_one[2] = list_two[2]  # [1,2,7], [5,6,7,8]
# Удалите из списка элемент с индексом [0].
del list_one[0]  # [2,7], [5,6,7,8]
# Удалите из списка элемент с предпоследним индексом.
del list_two[-2]  # [2,7], [5,6,8]
# Создайте третий список, который будет содержать в себе объединение двух прошлых списков.
list_three = list_one + list_two  # [2,7], [5,6,8], [2,7,5,6,8]
# Запросите у пользователя число и добавьте его в начало третьего списка.
list_three.insert(0, int(input("Введите число, которое добавится в начало списка: ")))  # [2,7], [5,6,8], [*, 2,7,5,6,8]
