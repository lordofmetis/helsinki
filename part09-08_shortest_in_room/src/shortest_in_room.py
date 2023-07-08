# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.people = []
        self.count = 0
        self.combined_height = 0

    def add(self, person: Person):
        self.people.append(person)
        self.count += 1
        self.combined_height += person.height

    def is_empty(self):
        if len(self.people) != 0:
            return False
        else:
            return True

    def shortest(self):
        shortest = [None, 10000]
        if self.is_empty():
            return None
        else:
            for ren in self.people:
                if ren.height < shortest[1]:
                    shortest[1] = ren.height
                    shortest[0] = ren
            return shortest[0]

    def remove_shortest(self):
        if self.is_empty():
            return None
        else:
            shortest = self.shortest()
            self.people.remove(shortest)
            return shortest

    def print_contents(self):
        print(
            f"There are {self.count} persons in the room, and their combined height is {self.combined_height} cm"
        )
        for ren in self.people:
            print(f"{ren.name} ({ren.height}cm)")


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
