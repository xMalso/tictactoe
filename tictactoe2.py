import time
def board():
	for i in range(3):
		for j in range(3):
			print("|{}".format(spots[i*3+j]),end="")
		print("|")
def whoisthere(spot):
	if spot == "X": return "1"
	return "2"
def checkwin():
	for combo in wins:
		if spots[combo[0]] != "_" and spots[combo[0]] == spots[combo[1]] == spots[combo[2]]:
			print("Player "+spots[combo[0]]+" has won the game")
			score[0 if spots[combo[0]] == "X" else 1] += 1
			return True
	return False
	
spots = ["_" for _ in range(9)]
wins = [(0, 4, 8),(2, 4, 6),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 1, 2),(3, 4, 5),(6, 7, 8)]
score = [0,0]
print("Formation")

for i in range(3):
	for j in range(3):
		print("|{}".format(i*3+j+1),end="")
	print("|")
turn = 0
xfirst = True
while True:
	pick = input("Pick a spot, 1-9: ")
	if not pick.isdigit():
		print("Must be a positive interger, ",end="")
	else:
		pick = int(pick) - 1
		if pick > 9 or pick < 0:
			print("Invalid value, ",end="")
		elif spots[pick] == "_":
			if turn%2==0: spots[pick] = "X"
			else: spots[pick] = "O"
			turn += 1
			board()
			win = checkwin()
			if win: turn = 10
			if turn >= 9 and xfirst or turn >= 8 and not xfirst:
				xfirst = not xfirst
				turn = xfirst - 1
				if not win: print("No winners, starting new game, "+("X" if xfirst else "O")+" will be starting first.")
				spots = ["_" for _ in range(9)]
				time.sleep(1)
				print("Score is "+str(score[0])+"-"+str(score[1])+" to X")
				time.sleep(1)
		else:
			print("This spot is taken, ",end="")