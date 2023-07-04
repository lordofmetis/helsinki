# Write your solution here
def generate_password(length: int):
    from random import sample
    from string import ascii_lowercase

    temp = sample(ascii_lowercase, length)

    empty = ""

    for i in temp:
        empty += i
    
    return empty

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))
