import random

PLAYER_ICON = ""
BOT_ICON = ""


def instruction():
	print("Welcome to GeekSchool TicTacToe!")
	print("Cells are numbered as follows:")
	brd_front = \
"""-------
|0|1|2|
-------
|3|4|5|
-------
|6|7|8|
-------"""
	print(brd_front)
	
	
def choose_icon():
	global PLAYER_ICON, BOT_ICON
	while True:
		choose = input("Choose your icon. Enter 'x' or 'o': ")
		if choose == "x":
			PLAYER_ICON = "X"
			BOT_ICON = "O"
			break
		elif choose == "o":
			PLAYER_ICON = "O"
			BOT_ICON = "X"
			break
		else:
			print("Invalid choose.")
	
	
def init_board():
	board = [" " for i in range(9)]
	return board


def display_board(board):
	for row in range(0,8,3):
		print("-------")
		for cell in range(3):
			print("|", end = "")
			print(board[row+cell], end = "")
		print("|")
	print("-------")


def winner(board):
	ways_to_win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
	for way in ways_to_win:
		if board[way[0]] == board[way[1]] == board[way[2]]:
			return board[way[0]]


def player_is_winner(board):
	return winner(board) == PLAYER_ICON


def bot_is_winner(board):
	return  winner(board) == BOT_ICON


def tie(board):
	return (not legal_moves(board)) and (not player_is_winner(board)) and (not bot_is_winner(board))


def legal_moves(board):
	ways_to_move = []
	for cell_index in range( len(board) ):
		if board[cell_index] == " ":
			ways_to_move.append(cell_index)
	return tuple(ways_to_move)


def bot_move(board):
	ways = legal_moves(board)
	if ways:
		cell = random.choice(ways)
		board[cell] = BOT_ICON


def player_move(board):
	ways = legal_moves(board)
	
	def to_str(x):
		return str(x)
	
	ways_s = map(to_str, ways)  # map(lambda x: str(x), ways)
	print("Your possible ways: " + " ".join(ways_s))
	while True:
		cell = int(input("Your way: "))
		if cell in ways:
			board[cell] = PLAYER_ICON
			break


instruction()
brd = init_board()
choose_icon()
if PLAYER_ICON == "X":
	while True:
		# Ход Игрока
		display_board(brd)
		player_move(brd)
		if player_is_winner(brd):
			display_board(brd)
			print("Ты выиграл!")
			break
		if tie(brd):
			display_board(brd)
			print("Ничья!")
			break
		# Ход бота
		display_board(brd)
		bot_move(brd)
		if bot_is_winner(brd):
			display_board(brd)
			print("Ты проиграл!")
			break
		if tie(brd):
			display_board(brd)
			print("Ничья!")
			break
elif BOT_ICON == "X":
	while True:
		# Ход бота
		display_board(brd)
		bot_move(brd)
		if bot_is_winner(brd):
			display_board(brd)
			print("Ты проиграл!")
			break
		if tie(brd):
			display_board(brd)
			print("Ничья!")
			break
		# Ход Игрока
		display_board(brd)
		player_move(brd)
		if player_is_winner(brd):
			display_board(brd)
			print("Ты выиграл!")
			break
		if tie(brd):
			display_board(brd)
			print("Ничья!")
			break
