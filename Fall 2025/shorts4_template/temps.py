"""Implement your class here"""
class Temp:
    def __init__(self, temp, unit):
        self._temp = temp
        self._unit = unit

    def _to_celsius(self):
        if self._unit == "C":
            return self._temp
        elif self._unit == "F":
            return (self._temp - 32) * 5 / 9

    def __str__(self):
        return f"{self._temp}{self._unit}"

    def __eq__(self, other):
        if not isinstance(other, Temp):
            return NotImplemented
        return self._to_celsius() == other._to_celsius()

    def __ne__(self, other):
        if not isinstance(other, Temp):
            return NotImplemented
        return self._to_celsius() != other._to_celsius()

    def __lt__(self, other):
        if not isinstance(other, Temp):
            return NotImplemented
        return self._to_celsius() < other._to_celsius()

    def __le__(self, other):
        if not isinstance(other, Temp):
            return NotImplemented
        return self._to_celsius() <= other._to_celsius()

    def __gt__(self, other):
        if not isinstance(other, Temp):
            return NotImplemented
        return self._to_celsius() > other._to_celsius()

    def __ge__(self, other):
        if not isinstance(other, Temp):
            return NotImplemented
        return self._to_celsius() >= other._to_celsius()