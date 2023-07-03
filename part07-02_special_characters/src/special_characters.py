# Write your solution here
def separate_characters(my_string: str):
    from string import ascii_letters, punctuation

    first = ""
    temp = ""
    second = ""
    final = ""

    for i in my_string:
        if i in ascii_letters:
            first += i
        else:
            temp += i
    
    for j in temp:
        if j in punctuation:
            second += j
        else:
            final += j

    return first, second, final

if __name__ == "__main__":
    parts = separate_characters("'abc', '', '.!åäö.!åäö'")
    print(parts[0])
    print(parts[1])
    print(parts[2])