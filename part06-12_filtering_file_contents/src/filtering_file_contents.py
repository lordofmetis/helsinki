# Write your solution here
def filter_solutions():
    correct_ones = []
    incorrect_ones = []

    with open("solutions.csv") as file:
        for line in file:
            parts = line.split(";")
            for part in parts:
                if "+" in part:
                    i = parts[1].find("+")
                    first = int(parts[1][: i])
                    third = int(parts[1][i + 1:])
                    result = int(parts[2])                    
                    if first + third == result:
                        correct_ones.append(line)
                    else:
                        incorrect_ones.append(line)
                
                elif "-" in part:
                    i = parts[1].find("-")
                    first = int(parts[1][: i])
                    third = int(parts[1][i + 1:])
                    result = int(parts[2])    
                    if first - third == result:
                        correct_ones.append(line)
                    else:
                        incorrect_ones.append(line)                    
    
    with open("correct.csv", "w") as correct_file:
        for correct_one in correct_ones:
            correct_file.write(correct_one)     
    with open("incorrect.csv", "w") as incorrect_file:
        for incorrect_one in incorrect_ones:
            incorrect_file.write(incorrect_one)           

if __name__ == "__main__":
    filter_solutions()