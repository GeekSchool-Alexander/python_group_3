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

choose_icon()
brd = init_board()
brd[2] = "X"
brd[4] = "X"
brd[7] = "X"
display_board(brd)
print(winner(brd), player_is_winner(brd), bot_is_winner(brd))
print(get_legal_moves(brd))
brd[0] = "O"
brd[6] = "O"
display_board(brd)
print(get_legal_moves(brd))
