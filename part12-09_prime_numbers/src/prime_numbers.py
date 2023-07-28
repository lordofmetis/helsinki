# Write your solution here
from math import sqrt

def prime_numbers():
    number = 2 
    while True:
        if all(number % i != 0 for i in range(2, int(sqrt(number)) + 1)):
            yield number
        number += 1


if __name__ == "__main__":
    numbers = prime_numbers()
    try:
        for i in range(8):
            print(next(numbers))
    except StopIteration:
        print("ran out of numbers")