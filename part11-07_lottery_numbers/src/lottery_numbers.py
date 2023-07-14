# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, weeks: int, correct_numbers: int):
        self.weeks = weeks
        self.correct_numbers = correct_numbers

    def number_of_hits(self, my_numbers: list):
        return sum([1 for number in my_numbers if number in self.correct_numbers])

    def hits_in_place(self, my_numbers: list):
        return [number if number in self.correct_numbers else -1 for number in my_numbers]

if __name__ == "__main__":
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))