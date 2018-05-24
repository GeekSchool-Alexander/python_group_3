import random

PLAYER_ICON = ""
BOT_ICON = ""


def choose_icon():
	global PLAYER_ICON, BOT_ICON
	while True:
		choose = input("Выбери 'O' или 'X': ")
		if choose == 'O' or choose == 'o':
			PLAYER_ICON = 'O'
			BOT_ICON = 'X'
			break
		elif choose == 'X' or choose == 'x':
			PLAYER_ICON = 'X'
			BOT_ICON = 'O'
			break
	

def init_board():
	board = []
	for cell in range(9):
		board.append(" ")
	return board
	
	
def display_board(board):
	for row in range(0, 8, 3):
		print("-------------")
		for cell in range(3):
			print("| ", end = "")
			print(board[row + cell] + " ", end = "")
		print('|')
	print("-------------")


def winner(board):
	ways_to_win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
	for way in ways_to_win:
		if board[way[0]] == board[way[1]] == board[way[2]]:
			return board[way[0]]


def player_is_winner(board):
	return winner(board) == PLAYER_ICON


def bot_is_winner(board):
	return winner(board) == BOT_ICON


def get_legal_moves(board):
	ways = []
	for index in range(len(board)):
		if board[index] == " ":
			ways.append(index)
	return tuple(ways)


def bot_move(board):
	ways = get_legal_moves(board)
	cell = random.choice(ways)
	board[cell] = BOT_ICON


def player_move(board):
	ways = get_legal_moves(board)  # Список свободных клеток
	# Вывод в консоль номеров свободных клеток
	print("Свободные клетки: ", end = " ")
	for way in ways:
		print(way, end = " ")
	# Выбор клетки для хода игроком
	while True:
		cell = int(input("\nВведите номер клетки для хода: "))
		if cell in ways:  # Если клетка свободна
			board[cell] = PLAYER_ICON  # Делаем ход в клетку
			break
		
choose_icon()
brd = init_board()
display_board(brd)
bot_move(brd)
display_board(brd)
bot_move(brd)
display_board(brd)
