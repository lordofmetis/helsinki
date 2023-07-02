# Write your solution here
def new_person(name: str, age: int):
    apple = (name, age)
    if name == "":
        raise ValueError
    elif " " not in name:
        raise ValueError
    elif len(name) >= 40:
        raise ValueError
    elif age < 0 or age >= 150:
        raise ValueError
    else:
        return apple

if __name__ == "__main__":
    old_person = new_person("James Jameson", 140)
    print(old_person)