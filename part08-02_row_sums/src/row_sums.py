# Write your solution here
def row_sums(my_matrix: list):

    for element in my_matrix:
        temp = 0
        for i in element:
            temp += i
        element.append(temp)

if __name__ == "__main__":
    my_matrix = [[1,2], [3,4]]
    row_sums(my_matrix)
    print(my_matrix)