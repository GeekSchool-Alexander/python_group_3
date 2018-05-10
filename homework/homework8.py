num_list = []
while True:
	num = int(input("Введите число: "))
	if num < 0:
		break
	else:
		num_list.append(num)
		
min = num_list[0]
half_size = len(num_list)//2

for num in num_list[:half_size]:
	if num < min:
		min = num

max = num_list[-1]

for num in num_list[half_size:]:
	if num > max:
		max = num

print("Minimal in 1-st half =  {}, maximal in 2-nd half = {}".format(min, max))
