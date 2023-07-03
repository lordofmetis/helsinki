# Write your solution here
def hypotenuse(leg1: float, leg2: float):
    from math import sqrt

    leg3 = sqrt(leg1 ** 2 + leg2 ** 2)
    return leg3

if __name__ == "__main__":
    print(hypotenuse(3,4))