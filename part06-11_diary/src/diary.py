# Write your solution here# Write your solution here
while True:
    
    print("1 - add an entry, 2 - read entries, 0 - quit")
    user_input = int(input("Function: "))
    
    if user_input == 1:
        diary_entry = input("Diary entry: ")
        with open("diary.txt", "a") as file:
            file.write(diary_entry)
            file.write("\n")
        print("Diary saved\n")
    
    elif user_input == 2:
        with open("diary.txt") as file:
            contents = file.read()
            print(f"Entries:\n{contents}")

    elif user_input == 0:
        print("Bye now!")
        break