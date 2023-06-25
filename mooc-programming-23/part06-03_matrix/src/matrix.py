# write your solution here
def row_sums():
    with open("matrix.txt") as file:
        empty = []
        for line in file:
            temp = 0
            parts = line.split(",")
            for part in parts:
                part = int(part)
                temp += part
            empty.append(temp)
        return empty

def matrix_max():
    with open("matrix.txt") as file:
        empty = []
        for line in file:
            parts = line.split(",")
            for part in parts:
                part = int(part)
                empty.append(part)
        return max(empty)

def matrix_sum():
    with open("matrix.txt") as file:
        empty = []
        final = 0
        for line in file:
            parts = line.split(",")
            for part in parts:
                part = int(part)
                empty.append(part)
        for i in empty:
            final += i
        return final

if __name__ == "__main__":
    row_sums()
    matrix_max()
    matrix_sum()


            
    

