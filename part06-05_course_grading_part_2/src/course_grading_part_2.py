# wwite your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    student_info = "students2.csv"
    exercise_data = "exercises2.csv"
    exam_points = "exam_points2.csv"

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
        exercises[parts[0]] = int(temp / 4)

points = {}
with open(exam_points) as last_file:
    for line in last_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        final = 0
        for part in parts[1: ]:
            final += int(part)
        points[parts[0]] = final

for pic, name in names.items():
    if pic in exercises:
        exercise = exercises[pic]
    if pic in points:
        point = points[pic]
    if 0 <= point + exercise <= 14:
        print(f"{name} 0")
    elif 15 <= point + exercise <= 17:
        print(f"{name} 1")
    elif 18 <= point + exercise <= 20:
        print(f"{name} 2")
    elif 21 <= point + exercise <= 23:
        print(f"{name} 3")
    elif 24 <= point + exercise <= 27:
        print(f"{name} 4")
    elif 28 <= point + exercise:
        print(f"{name} 5")
