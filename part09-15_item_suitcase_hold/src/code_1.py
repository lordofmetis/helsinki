# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.count = 0
        self.combined_weight = 0
        self.list = {}

    def add_item(self, item: Item):
        added_name = item.name()
        added_weight = item.weight()
        if self.combined_weight + added_weight <= self.max_weight:
            self.combined_weight += added_weight
            self.count += 1
            self.list[added_name] = added_weight

    def __str__(self):
        if self.count > 1:
            return f"{self.count} items ({self.combined_weight} kg)"
        else:
            return f"{self.count} item ({self.combined_weight} kg)"

    def print_items(self):
        for name, weight in self.list.items():
            print(f"{name} ({weight} kg)")

    def weight(self):
        return self.combined_weight

    def heaviest_item(self):
        if self.count == 0:
            return None
        else:    
            heaviest = [None, 0]
            for name, weight in self.list.items():
                if weight >= heaviest[1]:
                    heaviest[1] = weight
                    heaviest[0] = name
            return Item(heaviest[0], heaviest[1])


class CargoHold:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.combined_weight = 0
        self.count = 0
        self.list = {}

    def add_suitcase(self, suitcase: Suitcase):
        if self.combined_weight + suitcase.combined_weight <= self.max_weight:
            self.combined_weight += suitcase.combined_weight
            self.count += 1
            for name, weight in suitcase.list.items():
                self.list[name] = weight

        else:
            pass

    def __str__(self):
        if self.count != 1:
            return f"{self.count} suitcases, space for {self.max_weight - self.combined_weight} kg"     
        else:
            return f"{self.count} suitcase, space for {self.max_weight - self.combined_weight} kg"         

    def print_items(self):
        for name, weight in self.list.items():
            print(f"{name} ({weight} kg)")

if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
