# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:0>2} eur"

    def __eq__(self, another):
        return (self._euros == another._euros) and (self._cents == another._cents)

    def __ne__(self, another):
        return (self._euros != another._euros) or (self._cents != another._cents)

    def __lt__(self, another):
        if self._euros < another._euros:
            return True
        elif self._euros == another._euros:
            if self._cents < another._cents:
                return True
            else:
                return False
        else:
            return False

    def __ge__(self, another):
        if self._euros > another._euros:
            return True
        elif self._euros == another._euros:
            if self._cents > another._cents:
                return True
            else:
                return False
        else:
            return False

    def __add__(self, another):
        if self._cents + another._cents >= 100:
            return f"{self._euros + another._euros + 1}.{(self._cents + another._cents - 100):0>2} eur"
        else:
            return f"{self._euros + another._euros}.{(self._cents + another._cents):0>2} eur"

    def __sub__(self, another):
        if self.__lt__(another):
            raise ValueError("a negative result is not allowed")
        else:
            if self._cents - another._cents < 0:
                return f"{self._euros - another._euros - 1}.{(self._cents + 100 - another._cents):0>2} eur"
            else:
                return f"{self._euros - another._euros}.{(self._cents - another._cents):0>2} eur"


if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1