
color = ('black', 'white')
pieces = ('R', 'N', 'B', "K", "Q", "P")
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
rank = ("1","2","3","4","5","6","7","8")


class Piece:

	def __init__(self, color, square):
		if color == "black":
			self.color = -1
		else:
			self.color = 1
		self.square = square
		self.coords = square_to_coord(square)
		self.rank = self.coords[0]
		self.file = self.coords[1]
		self.justMoved = False

	def __str__(self):
		return self.name, self.color

	def move(self, new_square, board):
		board[self.coords[0]][self.coords[1]] = " "
		self.square = new_square
		self.coords = square_to_coord(self.square)
		board[self.coords[0]][self.coords[1]] = self

	def capture(self, square1, square2):
		pass


class Board:
	def __init__(self, player1, player2):
		self.board = []
		self.pieceList = []

		#creating the physical board
		for row in range(1, 10):
			r = []
			for n in range(1,10):
				r.append("\u2002")

			self.board.append(r)

		#setting the pieces of both players on the board
		for piece in player1.pieces:
			self.board[square_to_coord(piece.square)[0]][square_to_coord(piece.square)[1]] = piece
			self.pieceList.append(piece)

		for piece in player2.pieces:
			self.board[square_to_coord(piece.square)[0]][square_to_coord(piece.square)[1]] = piece
			self.pieceList.append(piece)

	def __str__(self):
		display = ""
		for row in self.board[::-1]:
			for piece in row:
				display += str(piece)
			display += "\n"

		#for row in self.board:
			#display.append(list(map(lambda x,y: x, self.board)))
		
		return display

	def display(self):
		display = []
		display.append([25*chr(9472)])
		for i in range(1,9):
			row = []
			row.append(chr(9474))
			for n in range(1,9):
				row.append(self.board[i][n])
				row.append(chr(9474))
			display.append(row)
			display.append([25*chr(9472)])

		for rows in display:
			for text in rows:
				print(text,end = "")
			print(" ")


	def place(self, *pieces):
		for piece in pieces:
			coords = piece.coords
			self.board[coords[0]][coords[1]] = piece

	def update(self, piece, square):
		self.board[square.row][square.column] = piece;

	def clear(self):
		for rank in self.board:
			for i in range(1,9):
				rank[i] = " "

	def reset(self):
		self.board = []
		self.board.append([""])
		self.board.append(['#', Piece("R", "black"), Piece('N', 'black'), Piece('B', 'black'), Piece('Q', 'black'), Piece('K', 'black'), Piece('B', 'black'), Piece('N', 'black'), Piece('R', 'black')])
		self.board.append(['#', 8*Piece('P', 'black')])
		self.board.append( 4*['#', '', '', '', '','','','','',''])
		self.board.append([8*Piece('P', 'white')])
		self.board.append([Piece('R', 'white'), Piece('N', 'white'), Piece('B', 'white'), Piece('Q', 'white'), Piece('K', 'white'), Piece('B', 'white'), Piece('N', 'white'), Piece('R', 'white')])

class Square:
	def __init__(self, row, column):
		self.row = row
		self.column = column
		self.coords = [ord(row) - 96, column]

	def __str__(self):
		return self.row + str(self.column)

class Player:
	def __init__(self, color, name = "Player"):
		self.name = name
		self.color = color
		
		#decide 1 or 8 depending on color
		self.number = int(str(ord(color[0]))[1])

		#adding pieces 
		self.pieces = [Rook(color, f"a{self.number}"), Rook(color, f"h{self.number}"), Knight(color, f"b{self.number}"), Knight(color, f"g{self.number}"), Bishop(color, f"c{self.number}"), Bishop(color, f"f{self.number}"), Queen(color, f"d{self.number}"), King(color, f"e{self.number}")]
		
		#adding pawns
		for file in letters:
			self.pieces.append(Pawn(color, f"{file}{self.number - ord(color[1]) / 2 + 53}"))

	def move(self):
		move = "Easter egg"
		#0: T/F
		#1: move/capture
		#2: piece
		#3: new square

		while validMove(move)[0] == False: 
			move = input("Input your next move: ")

		if validMove(move)[1] == "c":
			print(f"The {validMove(move)[2]} made capture on {validMove(move)[3]}")

		else:
			#board[][]
			#new_coords = square_to_coord(validMove(move)[3])
			
			#if validMove(move)[2] == ""
				#board[new_coords[0]][new_coords[1]] =
			pass  
			
		

class Pawn(Piece):
	def __init__(self, color, square):
		Piece.__init__(self, color, square)
		self.name = "P"
		self.value = 1
		self.move_count = 0

		if color == "black":
			self.color = -1
		else:
			self.color = 1

	def move(self, board, old_coord):
		potential_square = [old_coord[0], old_coord[1] + 1]
		if board[potential_square[0]][potential_square[1]] == '':
			board[potential_square[0]][potential_square[1]] = (self.name, self.color)
			board[old_coord[0], old_coord[1]]

	def capture(self):
		pass

	def __str__(self):
		if self.color == -1:
			return "\u265F"
		else:
			return "\u2659"

	def eligible_squares(self, board):
		ls = []
		
		#forward move
		if board[self.coords[0] + self.color][self.coords[1]] == " ":
			ls.append([self.coords[0] + self.color, self.coords[1]])

			#initial 2 squares move
			if self.move_count == 0 and board[self.coords[0] + 2 * self.color][self.coords[1]] == " ":
				ls.append([self.coords[0] + 2 * self.color, self.coords[1]])
		
		#capture squares
		if board[self.coords[0] + self.color][self.coords[1] + 1] != " " and :
			ls.append([self.coords[0] + self.color, self.coords[1] + 1])

		if board[self.coords[0] + self.color][self.coords[1] - 1] != " ":
			ls.append([self.coords[0] + self.color, self.coords[1] - 1]) 
		
		#en passant rule 
		if self.rank = 4.5 + 0.5 * self.color:
			if isinstance(board[self.rank][self.file + 1], Pawn) and board[self.rank][self.file + 1].color != self.color:
				enemy_pawn = board[self.rank][self.file + 1]
				if enemy_pawn.justMoved:
					ls.append([self.rank + self.color, self.file + 1])

			if isinstance(board[self.rank][self.file - 1], Pawn):
				enemy_pawn = board[self.rank][self.file - 1]
				if not enemy_pawn.justMoved:
					ls.append([self.rank + self.color, self.file - 1])

		for index in range(len(ls)):
			ls[index] = coord_to_square(ls[index])
		return ls

	def capture_squares(self):
		ls = []

		ls.append([self.coords[0] + 1, self.coords[1] + 1])
		ls.append([self.coords[0] + 1, self.coords[1] - 1])

		for index in range(len(ls)):
			ls[index] = coord_to_square(ls[index])
		return ls

class Knight(Piece):
	def __init__(self, color, square):
		Piece.__init__(self, color, square)
		self.name = "N"
		self.value = 3
		self.move_count = 0
		self.Square = Square

	def __str__(self):
		if self.color == -1:
			return "\u265E"
		else:
			return "\u2658"

	def eligible_squares(self):
		ls = [[1,2],[2,1],[-1,2],[-2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]]
		n = 0
		while n < len(ls):

			for i in range(2):
				ls[n][i] = ls[n][i] + square_to_coord(self.square)[i]
				
				if ls[n][i] < 1 or ls[n][i] > 8:
					ls.pop(n)
					n -= 1
					break

			n += 1
		
		for index in range(len(ls)):
			ls[index] = coord_to_square(ls[index])
		return ls

class Bishop(Piece):
	def __init__(self, color, square):
		Piece.__init__(self, color, square)
		self.name = "B"
		self.value = 3
		self.move_count = 0
		self.square = square

	def __str__(self):
		if self.color == -1:
			return "\u265D"
		else:
			return "\u2657"

	def eligible_squares(self, board):
		ls = []
		rank = square_to_coord(self.square)[0]
		file = square_to_coord(self.square)[1]

		#need to find a way to shorten this 4-time copy-pasted code

		for x in [1,-1]:
			for y in [1,-1]:
				coords = [rank, file]

				while 0 < coords[0] + x < 9 and 0 < coords[1] + y < 9:
					coords[0] += x  
					coords[1] += y 
					if board[coords[0]][coords[1]] != " " and board[coords[0]][coords[1]].color == self.color:
						break
					elif board[coords[0]][coords[1]] != " " and board[coords[0]][coords[1]].color != self.color:
						ls.append([coords[0], coords[1]]) 
						break
					else:
						ls.append([coords[0], coords[1]])

		for index in range(len(ls)):
			ls[index] = coord_to_square(ls[index])
		return ls


		

class Rook(Piece):
	def __init__(self, color, square):
		Piece.__init__(self, color, square)
		self.name = "R"
		self.value = 5
		self.move_count = 0
		self.square = square

	def __str__(self):
		if self.color == -1:
			return "\u265C"
		else:
			return "\u2656"

	def eligible_squares(self, board):
		ls = []

		rank = square_to_coord(self.square)[0]
		file = square_to_coord(self.square)[1]


		for x in [-1,1]:
			for index in range(2):
				coords = [rank, file]

				while 0 < coords[index] + x < 9:

					coords[index] += x 

					if board[coords[0]][coords[1]] != " " and board[coords[0]][coords[1]].color == self.color:
						break
					elif board[coords[0]][coords[1]] != " " and board[coords[0]][coords[1]].color != self.color:
						ls.append([coords[0], coords[1]]) 
						break
					else:
						ls.append([coords[0], coords[1]])

		for index in range(len(ls)):
			ls[index] = coord_to_square(ls[index])
		return ls

class Queen(Piece):
	def __init__(self, color, square):
		Piece.__init__(self, color, square)
		self.name = "Q"
		self.value = 9
		self.move_count = 0
		self.square = square

	def __str__(self):
		if self.color == -1:
			return "\u265B"
		else:
			return "\u2655"

	def eligible_squares(self, board):
		ls = []

		rank = square_to_coord(self.square)[0]
		file = square_to_coord(self.square)[1]


		for x in [-1,1]:
			for index in range(2):
				coords = [rank, file]

				while 0 < coords[index] + x < 9:

					coords[index] += x 

					if board[coords[0]][coords[1]] != " " and board[coords[0]][coords[1]].color == self.color:
						break
					elif board[coords[0]][coords[1]] != " " and board[coords[0]][coords[1]].color != self.color:
						ls.append([coords[0], coords[1]]) 
						break
					else:
						ls.append([coords[0], coords[1]])
		for x in [1,-1]:
			for y in [1,-1]:
				coords = [rank, file]

				while 0 < coords[0] + x < 9 and 0 < coords[1] + y < 9:
					coords[0] += x  
					coords[1] += y 
					if board[coords[0]][coords[1]] != " " and board[coords[0]][coords[1]].color == self.color:
						break
					elif board[coords[0]][coords[1]] != " " and board[coords[0]][coords[1]].color != self.color:
						ls.append([coords[0], coords[1]]) 
						break
					else:
						ls.append([coords[0], coords[1]])

		for index in range(len(ls)):
			ls[index] = coord_to_square(ls[index])
		return ls

class King(Piece):
	def __init__(self, color, square):
		Piece.__init__(self, color, square)
		self.name = "K"
		self.value = 0
		self.move_count = 0
		self.square = square

	def __str__(self):
		if self.color == -1:
			return "\u265A"
		else:
			return "\u2654"

	def eligible_square(self):
		ls = []

		#8 squares in each direction 

		#cannot enter squares threatened by other pieces

		#castling rule

#methods used

def square_to_coord(square):
	return [int(square[1]), ord(square[0]) - 96]

def coord_to_square(coord):
	return f"{chr(coord[1] + 96)}{coord[0]}"

def validMove(move):
	if len(move) == 2:

		if move[0] in letters and move[1] in rank:
			return (True, "m", "P", move)

		else:
			return (False, 0)

	elif len(move) == 3:

		if move[0] in pieces and move[1] in letters and move[2] in rank:
			return (True, "m", move[0], move[1:2])

		else:
			return (False, 0)

	elif len(move) == 4:

		if move[0] in pieces and move[1] == 'x' and move[2] in letters and move[3] in rank:
			coord = square_to_coord(move[2:3])
			#check if there is anything to capture at all
			if board[coord[1]][coord[0]] == " ":
				return (False, 0)
			else:
				return (True, "c", move[0], move[2:3])

		elif move[0] in letters and move[1] == 'x' and move[2] in letters and move[3] in rank and move[0] != move[2]:
			coord = square_to_coord(move[2:3])
			if board[coord[1]][coord[0]] == " ":
				return (False, 0)
			else:
				return (True, "c", "p", move[2:3])

		else:
			return (False, 0)

	else:
		return (False, 0)

def square_threatened(square, board):
	coords = square_to_coord(square)









#create both players
player1 = Player("white")
player2 = Player("black")
playerlist = [player1, player2]

#generate board
board = Board(player1, player2)
#board.clear()
#bishop = Bishop("white", "e5")

#knight = Knight("white", "f6")

#rook = Rook("black", "c7")

#queen = Queen("black", "c4")

#board.place(bishop, knight, rook, queen)

board.display()


#print(player1.number)
#for piece in player1.pieces:
#	print(piece)
#print(player2.number)
#for piece in player2.pieces:
#	print(piece)

#
#print(knight.eligible_squares())


#print(queen.eligible_squares(board.board))
