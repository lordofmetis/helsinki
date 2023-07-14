# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, date:int, month:int, year:int):
        self.date = date
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.date}.{self.month}.{self.year}"
    
    def __eq__(self, another):
        return (self.date == another.date) and (self.month == another.month) and (self.year == another.year)

    def __ne__(self, another):
        return (self.date != another.date) or (self.month != another.month) or (self.year != another.year)

    def __lt__(self, another):
        if self.year < another.year:
            return True
        elif self.year == another.year:
            if self.month < another.month:
                return True
            elif self.month == another.month:
                if self.date < another.date:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __gt__(self, another):
        if self.year > another.year:
            return True
        elif self.year == another.year:
            if self.month > another.month:
                return True
            elif self.month == another.month:
                if self.date > another.date:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(d1)
    print(d2)
    print(d1 == d2)
    print(d1 != d2)
    print(d1 == d3)
    print(d1 < d2)
    print(d1 > d2)