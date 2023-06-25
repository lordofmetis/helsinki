def palindromes(word):
    for i in range(len(word)):
        if word[i] != word[-i - 1]:
            return False
    return True

def main():
    while True:
        word = input("Please type in a word: ")
        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")

main()