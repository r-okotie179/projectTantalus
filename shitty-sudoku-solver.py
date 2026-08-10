'''
for each tile with index 0:
	i = 1 # iterate over digits 1 to 9
	if {no. i} | grid_i and column_i and row_i == 1:
		replace cell with numbercall this function again
		if no cells in grid == 0:	
			current grid construction
	else:	
		i += 1	## when the program is halted (assuming i am waiting for like 30 mins, i would like some structure of the code to be preserved so that I can see whatis happening	### better, i would like to see the changes totetoteh code happenighappenign dynamicall... thisithisis a visualisatonthng... how can this be achieved?
'''
    
# parse the .txt files (from project euler); when on laptop
sudoku_board = ["003020600","900305001","001806400","008102900","700000008","006708200","002609500","800203009","005010300"] 

# searching row by row (very naive appraoch)
p = []
for row in sudoku_board: 
    #row = str(row)
    if "0" in row:
        num = row.count("0")
        start = 0
        for each_zero in range(num):
            row_zero = sudoku_board.index(row)
            column_zero = row.index("0", start)
            start = column_zero + 1
            pos = (row_zero, column_zero)
            # now using the position, I can lock down the grid that this will form a part of
            # it would be easier to write a function of this passing the positions -- it would probably be smarter for this whole thing to be a function 
            p.append(pos)
            print(pos)
    else:
        pass
print(len(p))
#print(sudoku_board) # the modified list form