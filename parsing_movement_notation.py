pieces = ('R', 'N', 'B', "K", "Q")
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
rank = ("1","2","3","4","5","6","7","8")

def validMove(move):
	if len(move) == 2:

		#pawn move scenario (eg e4, e5)
		if move[0] in letters and move[1] in rank:
			return (True, "m", "P", move)

		else:
			return (False, 0)

	elif len(move) == 3:

		#piece move scenario (eg Qf7)
		if move[0] in pieces and move[1] in letters and move[2] in rank:
			return (True, "m", move[0], move[1:2])

		else:
			return (False, 0)

	elif len(move) == 4:

		#piece capture scenario (eg Nxe5)
		if move[0] in pieces and move[1] == 'x' and move[2] in letters and move[3] in rank:
			return (True, "c", move[0], move[2:3])
		
		#pawn capture scenario (eg exd5)
		elif move[0] in letters and move[1] == 'x' and move[2] in letters and move[3] in rank and move[0] != move[2]:
			return (True, "c", "p", move[2:3])
		
		#scenario like Nbg2 or Rgh8
		elif (move[0] == "N" or "R") and move[1] in letters and move[2] in letters and move[3] in rank and move[1] != move[2]:
			return (True, "m", move[0], move[2:3])

		#scenario like R5h8
		elif move[0] == "R" and move[1] in rank and move[2] in letters and move[3] in rank and move[1] != move[3]:
			return (True, "m", move[0], move[2:3])

		else:
			return (False, 0)

	else:
		return (False, 0)


move = "Easter egg"
while validMove(move)[0] == False: 
	move = input("Input your next move: ")

if validMove(move)[1] == "c":
	print(f"The {validMove(move)[2]} made capture on {validMove(move)[3]}")

else:
	print(f"The {validMove(move)[2]} moved to {validMove(move)[3]}")





