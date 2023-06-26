# write your solution here

user_input = input("Write text: ")
parts = user_input.split(" ")

with open("wordlist.txt") as file:
    for part in parts:
        if part in file:
            part = f"*{part}*"
    print(user_input)