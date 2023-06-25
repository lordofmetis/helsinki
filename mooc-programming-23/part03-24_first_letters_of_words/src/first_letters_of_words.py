# Write your solution here

string = input("Please type in a sentence: ")

length = len(string)

index = 0

character = string[index]

print(character)

while True:
    
    if index + 1 == length:
        break

    if character == " ":
        print(string[(index + 1)])
    index += 1
    
