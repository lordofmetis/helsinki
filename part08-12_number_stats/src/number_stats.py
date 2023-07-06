class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum = 0

    def add_number(self, number: int):
        self.numbers += 1
        self.sum += number

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        return self.sum

    def average(self):
        try:
            return (self.sum / self.numbers)
        except ZeroDivisionError:
            pass
    
    def input_test(self):
        count = 0
        total_odd = 0
        total_even = 0

        while True:
            user_input = int(input(""))
            if user_input == -1:
                break
            count += 1
            if user_input % 2 == 0:
                total_even += user_input
            else:
                total_odd += user_input
        print(f"Sum of numbers: {total_odd + total_even}")
        print(f"Mean of numbers: {(total_odd + total_even) / count}")
        print(f"Sum of even numbers: {total_even}")
        print(f"Sum of odd numbers: {total_odd}")

stats = NumberStats()
print("Please type in integer numbers: ")
stats.input_test()