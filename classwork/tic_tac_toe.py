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
		print("-------")
		for cell in range(3):
			print("|", end = "")
			print(board[row+cell], end = "")
		print('|')
	print("-------")
	
	
choose_icon()
print(PLAYER_ICON, BOT_ICON)
brd = init_board()
print(brd)
display_board(brd)
brd[5] = PLAYER_ICON
brd[2] = BOT_ICON
display_board(brd)