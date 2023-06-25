# Write your solution here
def row_correct(sudoku: list, row_no: int):
    test = []

    row = sudoku[row_no]
    for item in row:
        if item > 0:
            test.append(item)
    test_again = sorted(set(test))
    if sorted(test) == list(test_again):
        return True
    else:
        return False

def column_correct(sudoku: list, column_no: int):
    test = []

    for i in range(len(sudoku)):
        if sudoku[i][column_no] > 0 and sudoku[i][column_no] in test:
            return False
        test.append(sudoku[i][column_no])
    
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    temporary = []
    test = []

    i = row_no
    j = column_no

    n = 0
    while n < 3:  
        m = 0  
        while m < 3:  
            temporary.append(sudoku[i][j + m])
            m += 1
        i += 1  
        n += 1

    for w in temporary:
        if w > 0 and w in test:
            return False
        test.append(w)
    return True

def sudoku_grid_correct(sudoku: list):
    # Check all rows and columns
    for i in range(len(sudoku)):
        if not row_correct(sudoku, i) or not column_correct(sudoku, i):
            return False

    # Check all 3x3 blocks
    for row_no in range(0, len(sudoku), 3):
        for column_no in range(0, len(sudoku[row_no]), 3):
            if not block_correct(sudoku, row_no, column_no):
                return False

    return True

if __name__ == "__main__":
    # ... (your sudoku1 definition here) ...

    print(sudoku_grid_correct(sudoku1))  # False

if __name__ == "__main__":
    sudoku1 = [
        [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
        [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
        [ 0, 5, 1, 6, 0, 0, 8, 3, 9 ],
        [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
        [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
        [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
        [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
        [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
        [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]

    print(sudoku_grid_correct(sudoku1))