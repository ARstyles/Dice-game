from pprint import pprint

def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet -> -1
    # return row, col tuple (or (None, None) if there is none)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None  # if no space in the puzzle is empty (-1)

def is_valid(puzzle, guess, row, col):
    # figures whether the guess at row/col is a valid guess or not
    # returns true if valid, false otherwise

    # row part
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # col part
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # square part
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)  # step 1 to choose where on the puzzle to make a guess
    # step 1.1: if there's nowhere, then we're done because we allowed only valid inputs
    if row is None:
        return True
    
    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):  # range(1, 10) is 1, 2, 3, ..., 9
        # step 3: check if this is valid
        if is_valid(puzzle, guess, row, col):
            # if this is valid, then place that guess on the puzzle
            puzzle[row][col] = guess  # now recurse using this puzzle
            # step 4: recursively call our function 
            if solve_sudoku(puzzle):
                return True
        # if puzzle is not solved, then backtrack and try a new number
        puzzle[row][col] = -1
    return False

# example board
if __name__ == '__main__':
    example_board = [
        [5, 3, -1, -1, 7, -1, -1, -1, -1],
        [6, -1, -1, 1, 9, 5, -1, -1, -1],
        [-1, 9, 8, -1, -1, -1, -1, 6, -1],
        [8, -1, -1, -1, 6, -1, -1, -1, 3],
        [4, -1, -1, 8, -1, 3, -1, -1, 1],
        [7, -1, -1, -1, 2, -1, -1, -1, 6],
        [-1, 6, -1, -1, -1, -1, 2, 8, -1],
        [-1, -1, -1, 4, 1, 9, -1, -1, 5],
        [-1, -1, -1, -1, 8, -1, -1, 7, 9]
    ]
    
    solve_sudoku(example_board)
    pprint(example_board)
