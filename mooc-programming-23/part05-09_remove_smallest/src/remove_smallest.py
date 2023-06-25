# Write your solution here
def remove_smallest(numbers: list):
    numbers.remove(min(numbers))

if __name__ == "__main__":
    numbers = [1, 2, 3, 5, 6]
    remove_smallest(numbers)
    print(numbers)