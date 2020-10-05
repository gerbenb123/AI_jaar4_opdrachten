import numpy as np

# place triominoes in matrix 3 rows x 4 cols
NR_OF_COLS = 16 # 4 triominoes HB VB L RL + 12 cells
NR_OF_ROWS = 22 # 6*HB 4*VB 6*L 6*RL

triominoes = [np.array(trio) for trio in [
        # horizontal bar (HB)
        [[1,1,1]],
        # vertical bar (VB)
        [[1],[1],[1]],
        # normal L (L)
        [[1,0], [1,1]],
        # rotated L (RL)
        [[1,1], [0,1]] ]]

def all_positions(T):
    # find all positions to place triomino T in matrix M (3 rows x 4 cols)

    rows, cols = T.shape
    for i in range(3+1 - rows):
        for j in range(4+1 - cols):
            M = np.zeros((3, 4), dtype='int')
            # place T in M
            M[i:i+rows, j:j+cols] = T
            yield M

# matrix rows has 22 rows x 16 cols 
# and has the following cols: HB VB L RL (0,0) (0,1) (0,2) (0,3) (1,0) .... (3,3)
rows = []

for i, P in enumerate(triominoes):
    # i points to the 4 triominoes HB VB L RL
    for A in all_positions(P):

        # add 4 zeros to each row
        A = np.append(np.zeros(4, dtype='int'), A)
        A[i] = 1
        rows.append(list(A))


aaa = np.array(rows)
print(aaa)
#print()

# note that zip(*b) is the transpose of b
cols = [list(i) for i in zip(*rows)]

# note that when applying alg-x we're only interested in 1's
# so we add 2 lists that define where the 1's are

def find_ones(rows):
    lv_row_has_1_at = []
    for row in rows:
        x = []
        for i in range(len(row)):
            if row[i] == 1:
                x.append(i)
        lv_row_has_1_at.append(x.copy())
    return lv_row_has_1_at

 

row_has_1_at = find_ones(rows) # global read-only
col_has_1_at = find_ones(cols) # global read-only

for r in row_has_1_at:
    assert len(r) == 4

rows_valid = NR_OF_ROWS * [1]
cols_valid = NR_OF_COLS * [1]

all_solutions = []

def cover(r, row_valid, col_valid):

    # given the selected row r set related cols and rows invalid
    # appr. 75% of the time is spent in this function
    row_valid[r]= 0
    row_location_of1s = row_has_1_at[r]

    #for elke colom waar row een 1 heeft       

    for i in row_location_of1s:
        #cover all rows that overlap with row r
        row_index = 0

        #colomn posities met 1
        for row in row_has_1_at:
            if i in row:
                row_valid[row_index]=0
            row_index = row_index +1

        #cover all cols that have a 1 in row r
        # col_index = 0
        # for col in col_has_1_at:
        #     if r in col:
        #         col_valid[col_index] = 0
        #     col_index = col_index +1
        col_valid[i] = 0

 

    # for index in range(col_valid):

    #    for rowindex in range(row_valid):

    #     if all(value == 0 for value in col_valid): 
    #         #and all(value == 0 for value in row_valid):
    #         #print (solution)
    #         print("finished? exact cover is found ?")
    #         all_solutions.append(solution)
    #         return True

    

    pass

 

  

def solve(row_valid, col_valid, solution):

    if all(value == 0 for value in col_valid) and  all(value == 0 for value in row_valid):
        #print(np.array(solution))
        #print_one_solution(solution)
        all_solutions.append(solution.copy())
        return

    if all(value == 0 for value in row_valid):

        return
    #Select column
    smallestcolumn_size = 1000
    columIndex=0

    for x in col_valid:
        if x == 1:
            #get smallest nr of 1 in colomn
            numOfOnes = 0
            for y in range(len(row_valid)):
                if y in col_has_1_at[columIndex] and row_valid[y] == 1:
                    numOfOnes=numOfOnes+1
            if numOfOnes == 0:
                #(" geen 1´s" )
                return False
            if numOfOnes < smallestcolumn_size:
                smallestcolumn_size = numOfOnes
                smallestcolumn_index = columIndex
        columIndex = columIndex+1

    #kleinste colomn gevonden.
    row_location_of_column = col_has_1_at[smallestcolumn_index]

    for rowindex in row_location_of_column:
        if row_valid[rowindex] == 0:
            continue

        partial_row_valid = list(row_valid)
        partial_col_valid = list(col_valid)
        #cover row r and add partial solution

        partial_row_valid[rowindex] = 0
        solution.append(rowindex)
        #lokaties van 1 in geselecteerde row:
        column_locations_of_row = row_has_1_at[rowindex]
        #cover all rows that overlap with row r
        b = 0

        for row_1locations in row_has_1_at:
            for x in column_locations_of_row:
                if x in row_1locations:
                    partial_row_valid[b]=0
            b = b+1

        for x in column_locations_of_row:
            partial_col_valid[x] = 0

        solve(partial_row_valid, partial_col_valid, solution)
        solution.pop()


def print_one_solution(solution):
    # place triominoes in matrix 3 rows x 4 cols
    D = [[0 for i in range(4)] for j in range(3)]
    for row_number in solution:
        #print(row_number) # 1 6 14 21
        row_list = row_has_1_at[row_number]
        #print(row_list)   # 0 5 6 7
        idx = row_list[0]
        assert idx in [0,1,2,3]
        symbol = ['HB','VB','L ','RL'][idx]
        for c in row_list[1:]: # skip first one

            rownr = c//4-1
            colnr = c%4
            D[rownr][colnr] = symbol

    print('------------------------')

    for i in D:
        print(i)

solve(rows_valid, cols_valid, [])

for solution in all_solutions:
    # solutions are sorted
    print_one_solution(solution)
    print()