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
        if name not in my_dictionary:
            my_dictionary[name] = []
        my_dictionary[name].append(number)
        print("ok!")
    elif command == 1:
        name = input("name: ")
        if name in my_dictionary:
            print("\n".join(my_dictionary[name]))
        else:
            print("no number")


