while True:
    number = int(input("Please type in a number: "))

    if number <= 0:
        print("Thanks and bye!")
        break

    original = number
    factorial = 1

    while number > 0:
        factorial *= number
        number -= 1

    print(f"The factorial of the number {original} is {factorial}")