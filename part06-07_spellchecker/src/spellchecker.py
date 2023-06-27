# write your solution here
if True:
    user_input = input("Write text: ")
else:
    user_input = "I have a gii epsianl"

parts = user_input.split(" ")
dictionary = []
with open("wordlist.txt") as file:
    for line in file:
        line = line.strip("\n")
        dictionary.append(line.lower())

updated_user_input = user_input

for part in parts:
    if part.lower() not in dictionary:
        updated_user_input = updated_user_input.replace(part, f"*{part}*")

print(updated_user_input)