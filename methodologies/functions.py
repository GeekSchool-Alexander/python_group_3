import random
from time import *
alien_HP = 5
alien_name = "Zim"
alien_mood_is_good = True

man_HP = 3
man_name = "Толя"


# def - define - определение
# def имя_функции(параметры):
def alien_say_hi(mood, name = "человек"):  # Определение функции
	if mood:
		print("Привет, "+name+". Я пришел с миром!")
	else:
		print("Привет, человек. Отдай мне свой мир.")

def man_shoot():
	global alien_HP
	sit = random.randint(0, 3)
	if sit == 0:
		alien_HP -= 1
		print("Инопланетянин: АЙ. ПОПАЛИ!")
	else:
		print("Инопланетянин: БУГАГА! НЕ ПОПАЛ!")

def alien_shoot():
	global man_HP
	sit = random.randint(0, 6)
	if sit == 0:
		man_HP -= 1
		print("Человек: Ты попал по мне!")
	else:
		print("Человек: Не попал! Не попал!")


# Вызовы функции
alien_say_hi(alien_mood_is_good, man_name)

while man_HP > 0 and alien_HP > 0:
	man_shoot()
	alien_shoot()
