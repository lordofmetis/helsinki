# Write your solution here
def double_items(numbers: list):
    new_numbers = numbers[ : ]
    test = []
    for i in new_numbers:
        test.append(i * 2)

    return test


if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)