import random
my_num = random.randint(1, 30)
continue_game = True
while continue_game:
    n = int( input( 'Угадайте число: ' ) )
    if n == my_num:
        print('Ты выиграл! :)')
        continue_game = False
    elif abs(n - my_num) <= 10:
        print('Горячо. Попробуй еще раз.')
    elif 10 < abs(n - my_num) <= 20:
        print('Тепло. Попробуй еще раз.')
    elif 20 < abs(n - my_num) <= 30:
        print('Прохладно. Попробуй еще раз.')
    else:
        print('Холодно. Попробуй еще раз.')
print("Программа завершена.")