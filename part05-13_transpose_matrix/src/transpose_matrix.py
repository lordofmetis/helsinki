def transpose(matrix: list):
    # Get the number of rows and columns in the original matrix
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    # Initialize the transposed matrix with the correct dimensions
    transposed = []
    for col in range(num_columns):
        transposed_row = []
        for row in range(num_rows):
            transposed_row.append(0)
        transposed.append(transposed_row)

    # Iterate through the original matrix and fill the transposed matrix
    for row in range(num_rows):
        for col in range(num_columns):
            transposed[col][row] = matrix[row][col]

    # Update the original matrix with the transposed matrix
    matrix[:] = transposed

if __name__ == "__main__":
    matrix = [
        [1, 2, 3,],
        [4, 5, 6,],
        [7, 8, 9,]
    ]
    print(transpose(matrix))
