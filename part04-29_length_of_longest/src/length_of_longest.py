# Write your solution here
def length_of_longest(my_list):
    longest = my_list[0]
    for item in my_list:
        if len(item) > len(longest):
            longest = item
    return len(longest)


if __name__ == "__main__":
    my_list = ['Alan', 'Grace', 'Frances', 'Kim', 'Susan']

    result = length_of_longest(my_list)
    print(result)