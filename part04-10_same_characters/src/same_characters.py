# Write your solution here
def same_chars(word, a, b):
    length = len(word)
    if a < 0 or b < 0 or a >= length or b >= length:
        return False
    elif word[a] == word[b]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))