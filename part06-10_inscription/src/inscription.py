# Write your solution here
user_input = input("Whom should I assign this to: ")
input_user = input("Where shall I save it: ")

with open(input_user, "w") as file:
    file.write(f"Hi {user_input}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")