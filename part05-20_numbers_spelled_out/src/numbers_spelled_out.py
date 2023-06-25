# Write your solution here
def dict_of_numbers():
    dict_of_numbers = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
        12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
        17: "seventeen", 18: "eighteen", 19: "nineteen"
    }

    figures = {20: "twenty",30: "thirty",40: "forty",50: "fifty",60: "sixty",70: "seventy",80: "eighty",90: "ninety"}

    shuzi = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

    for i in figures:
        for j in shuzi:
            if j == 0:
                dict_of_numbers[i] = figures[i]
            else:
                dict_of_numbers[i + j] = figures[i] + "-" + shuzi[j]
    
    return dict_of_numbers

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])