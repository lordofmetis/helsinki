# Write your solution here
def add_student(students: dict, name: str):
    students[name] = []
    
def add_course(students: dict, name: str, completion: tuple):
    course, grade = completion
    students[name].append(completion)

def print_student(students: dict, name: str):
    counter = []
    for j in students[name]:
        if j[1] > 0:
            counter.append(students[name])
    print(f"{name}:")
    print(f" {len(counter)} completed courses:")
    total = 0
    for i in students[name]:
        if i[1] > 0:
            print(f"  {i[0]} {i[1]}")
            total += i[1]
    print(f" average grade {total / len(counter)}")
    
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Peter")