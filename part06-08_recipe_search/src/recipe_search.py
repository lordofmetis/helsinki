def search_by_name(filename: str, word: str):
    temp = []
    final = []
    word = word.lower()

    with open(filename) as file:
        for line in file:
            line = line.strip().lower()
            temp.append(line)

    in_recipe_name = True
    for i in temp:
        if i == "":
            in_recipe_name = True
        elif in_recipe_name:
            if word in i:
                final.append(i)
            in_recipe_name = False

    return final

def search_by_time(filename: str, prep_time: int):

    temp = []
    final = []

    with open(filename) as file:
        for line in file:
            line = line.strip()
            temp.append(line)

    if int(temp[1]) <= prep_time:
        final.append(f"{temp[0]}, preparation time {temp[1]} min")
    for i in range(len(temp)):
        if temp[i] == "":
            mark = int(temp[i + 2])
            if mark <= prep_time:
                final.append(f"{temp[i + 1]}, preparation time {mark} min")

    return final

if __name__ == "__main__":
    found_recipes = search_by_time("recipes1.txt", 80)

    for recipe in found_recipes:
        print(recipe)