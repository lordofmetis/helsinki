# Write your solution here

string = input("Word: ")
length = len(string)

print("*" * 30)

print("*" + int((28 - length) / 2) * str(" ") + string + int((28 - length) / 2) * str(" ") + "*")

print("*" * 30)