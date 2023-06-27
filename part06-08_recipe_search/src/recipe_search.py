def search_by_name(filename: str, word: str):
    temp = []
    final = []
    word = word.lower()

    with open(filename) as file:
        for line in file:
            line = line.strip()
            temp.append(line)

    in_recipe_name = True
    for i in temp:
        if i == "":
            in_recipe_name = True
        elif in_recipe_name:
            if word in i.lower():
                final.append(i)
            in_recipe_name = False

    return final

if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")

    for recipe in found_recipes:
        print(recipe)