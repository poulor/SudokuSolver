board = [
	[7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bd):
	for i in range(len(bd)):
		if i % 3 == 0:
			print(" - - - - - - - - - - - - - - ")

		for j in range(len(bd[i])):
			if j % 3 == 0:
				print(" | ", end="")
			if j == 8:
				print("{} |".format(bd[i][j]))
			else:
				print("{} ".format(bd[i][j]), end="")        
		
		print(" - - - - - - - - - - - - - - ")

if __name__ == "__main__":
    print_board(board)
