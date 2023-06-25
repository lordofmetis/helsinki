# Write your solution here

string = ""
length = 1

while length != 0:
    string = input("Please type in a string: ")
    length = len(string)
    print("\n" + string + "\n" + "-" * length + "\n")