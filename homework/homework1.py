# Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No".
var_int = 10
var_float = 8.4
var_str = "No"
# Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза, результат свяжите с переменной big_int. Сама var_int измениться не должна.
big_int = var_int * 3.5
# Измените значение, хранимое в переменной var_float, уменьшив его на единицу, результат свяжите с той же переменной.
var_float = var_float - 1
# Разделите var_int на var_float, а затем big_int на var_float и выведите результат вычислений в консоль. Результат данных выражений не привязывайте ни к каким переменным.
print(var_int/var_float, big_int/var_float)
# Выведите значения всех переменных в консоль.
print(var_int, var_float, var_str, big_int, var_float)
