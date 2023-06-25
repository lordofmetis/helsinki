# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        empty = []
        for line in new_file:
            empty.append(int(line))
        return max(empty)