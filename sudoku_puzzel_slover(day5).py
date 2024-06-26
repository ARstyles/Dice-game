def find_next_empty(puzzel):
    #finds the next row,col on the puzzel that's not filled yet -> -1
    #return row,col tuple (or (none,none) if there is none)
    for r in range(9):
        for c in range(9):
            if puzzel[r][c] == -1:
                return r,c
    return None,None #if no space in the puzzel are empty(-1)

def slove_sudoku(puzzel):
    row,col = find_next_empty(puzzel)  #to choose where on the puzzel to make a guess