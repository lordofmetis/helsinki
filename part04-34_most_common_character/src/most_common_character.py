# Write your solution here
def most_common_character(string):
    comeon = string[0]
    for i in range(len(string)):
        if string.count(string[i]) >= string.count(comeon):
            comeon = string[i]
    return comeon

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))