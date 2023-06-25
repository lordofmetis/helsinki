def all_the_longest(strings_list):
    longest_strings = []
    max_length = 0

    for string in strings_list:
        if len(string) > max_length:
            max_length = len(string)
            longest_strings = [string]  
        elif len(string) == max_length:
            longest_strings.append(string)  

    return longest_strings

#
if __name__ == "__main__":
    my_list = ["abc", "def", "ghijk", "lmnop", "qrstu", "vwxyz"]
    result = all_the_longest(my_list)
    print(result) 