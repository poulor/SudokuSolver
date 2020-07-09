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

def solve_board(bd):

    empty_space_pos = find_empty_space(bd)

    if not empty_space_pos:
        print("Board solved!")
        return True
    
    for num in range (1,10):
        if is_valid_addition(bd, num, empty_space_pos):
            add_number_to_board(bd, num, empty_space_pos)
            
            if solve_board(bd):
                return True

            bd[empty_space_pos[0]][empty_space_pos[1]] = 0

    return False    

def add_number_to_board(bd, num, pos):
    bd[pos[0]][pos[1]] = num

def is_empty_space(bd, pos):
	return bd[pos[0]][pos[1]] == 0

def find_empty_space(bd):
	for i in range(len(bd)):
		for j in range(len(bd[i])):
			if is_empty_space(bd,(i,j)):
				return (i,j)
	
	return None

def is_valid_addition(bd, num, pos):
	# Checking if row is valid after adding
	for i in range(len(bd[pos[0]])):

		# if bd[pos[0]][i] == num and pos[1] != i:
		if bd[pos[0]][i] == num:			
			return False

	# Checking if column is valid after adding
	for i in range(len(bd)):
		
		# if bd[i][pos[1]] == num and pos[0] != i:
		if bd[i][pos[1]] == num:
			return False

	# Checking square is valid after adding
	square_start_row_pos = pos[0] - (pos[0] % 3)
	square_start_col_pos = pos[1] - (pos[1] % 3)
	square_start_pos = (square_start_row_pos,square_start_col_pos) # (row, column)

	for i in range(square_start_pos[0], square_start_pos[0] + 3):
		for j in range(square_start_pos[1], square_start_pos[1] + 3):
		
			# if bd[i][j] == num and (i,j) != pos:
			if bd[i][j] == num:
				return False


	# # Check box
	# box_x = pos[1] // 3
	# box_y = pos[0] // 3

	# for i in range(box_y*3, box_y*3 + 3):
	# 	for j in range(box_x * 3, box_x*3 + 3):
	# 		if bd[i][j] == num and (i,j) != pos:
	# 			return False

	return True

if __name__ == "__main__":
    print_board(board)
    solve_board(board)
    print()
    print_board(board)
