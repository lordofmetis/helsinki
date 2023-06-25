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

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))