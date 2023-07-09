# WRITE YOUR SOLUTION HERE:
class ListHelper:
    def __init__(self):
        pass

    @classmethod
    def greatest_frequency(cls, numbers: list):
        temp = {}
        for number in numbers:
            if number not in temp:
                temp[number] = 1
            else:
                temp[number] += 1

        max_count = max(temp.values())
        for number, count in temp.items():
            if count == max_count:
                return number

    @classmethod
    def doubles(cls, numbers: list):
        temp = {}
        for number in numbers:
            if number not in temp:
                temp[number] = 1
            else:
                temp[number] += 1

        return len([number for number, count in temp.items() if count >= 2])

if __name__ == "__main__":
    numbers = [3, 2, 3, 2, 2, 3, 2, 2, 1, 1, 2]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
