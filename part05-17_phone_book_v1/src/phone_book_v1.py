# Write your solution here

my_dictionary = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3:
        print("quitting...")
        break    
    elif command == 2:
        name = input("name: ")
        number = input("number: ")
        my_dictionary[name] = number
        print("ok!")
    elif command == 1:
        name = input("name: ")
        if name in my_dictionary:
            print(my_dictionary[name])
        else:
            print("no number")


