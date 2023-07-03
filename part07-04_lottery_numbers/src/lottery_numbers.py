# Write your solution here
def lottery_numbers(amount: int, lower: int, upper: int):
    from random import sample
    
    empty = []
    
    numbers = list(range(lower, upper + 1))
    samplee = sample(numbers, amount)

    samplee = sorted(samplee)

    return samplee
    
if __name__ == "__main__":
    for number in lottery_numbers(1, 1, 10):
        print(number)