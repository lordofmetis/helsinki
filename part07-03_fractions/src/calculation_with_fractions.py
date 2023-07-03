# Write your solution here
def fractionate(amount: int):
    from fractions import Fraction

    empty = []

    for _ in range(amount):
        empty.append(Fraction(1, amount))
        
    return empty

if __name__ == "__main__":
    print(fractionate(5))