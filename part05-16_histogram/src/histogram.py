def histogram(string):
    temporary = {}

    for character in string:
        if character not in temporary:
            temporary[character] = 0  # Initialize the count to 0 for a new character
        temporary[character] += 1  # Increment the count for the character
    
    for character, count in temporary.items():
        print(character, '*' * count)  # Print the character and the '*' character repeated 'count' times
