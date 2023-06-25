# write your solution here
def read_fruits():
    with open("fruits.csv") as file:
        catalogue = {}
        for line in file:
            parts = line.split(";")
            name = parts[0]
            price = float(parts[1])
            catalogue[name] = price
        return catalogue

