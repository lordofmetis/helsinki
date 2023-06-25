def inputs(point, exercise):
    points = []
    exercises = []

    while True:
        input_values = input("Exam points and exercises completed: ").split()
    
        if not input_values:
            print("Statistics: ")
            break
    
        x, y = input_values
        point = int(x)
        exercise = int(y)

        points.append[point]
        exercises.append[exercise]

        return points, exercises

def grade(point, exercise):
    exercise_point = exercise * 0.1
    total_point = point + exercise
    print("Grade distribution: ")
    if total_point >= 0 and total_point < 14:
        



def main():
