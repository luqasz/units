import decimal
from units.si import prefix

class AbstractUnit:

    def __init__(self, value: float, symbol: str):
        self.value = float(value)
        self.symbol = symbol

    def __str__(self):
        pref = prefix.by_exp[decimal.Decimal(self.value).adjusted()]
        value = (self.value / pow(10, pref.exp))
        return f"{value} {pref}{self.symbol}"

    def __add__(self, other):
        value = self.value + other.value
        return AbstractUnit(value=value, symbol=self.symbol)

    def __sub__(self, other):
        value = self.value - other.value
        return AbstractUnit(value=value, symbol=self.symbol)

    def __mul__(self, other):
        value = self.value * other
        return AbstractUnit(value=value, symbol=self.symbol)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __float__(self):
        return float(self.value)

    def __hash__(self):
        return hash((self.value, self.symbol))
