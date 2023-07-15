# WRITE YOUR SOLUTION HERE:
import string

def most_common_words(filename: str, lower_limit: int):
    temp = []

    with open(filename) as file:
        for line in file:
            parts = line.split()
            for part in parts:
                if part[-1] in string.punctuation:    
                    part = part[:-1]
                temp.append(part)

    return {word: temp.count(word) for word in temp if temp.count(word) >= lower_limit}

if __name__ == "__main__":
    most_common_words("comprehensions.txt", 3)
