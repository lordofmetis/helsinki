# Write your solution here
def read_input(user_input: str, lower: int, higher: int):
    while True:
        try:
            number = int(input(user_input))
            if number > lower and number < higher:
                return number
            else:
                print(f"You must type in an integer between {lower} and {higher}")
        except ValueError:
            print(f"You must type in an integer between {lower} and {higher}")

if __name__ == "__main__":
    number = read_input("Enter a number: ", 5, 10)
    print("You typed in:", number)