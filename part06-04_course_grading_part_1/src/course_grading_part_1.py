# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

names = {}
with open(student_info) as left_file:
    for line in left_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        names[parts[0]] = parts[1] + " " + parts[2].strip()

exercises = {}
with open(exercise_data) as right_file:
    for line in right_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        temp = 0
        for part in parts[1: ]:
            temp += int(part)
        exercises[parts[0]] = temp

for pic, name in names.items():
    if pic in exercises:
        exercise = exercises[pic]
    print(f"{name} {exercise}")
