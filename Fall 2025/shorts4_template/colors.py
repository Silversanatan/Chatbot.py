class Color:
    def _clamp(self, value):
        if value < 0:
            return 0
        if value > 255:
            return 255
        return value

    def __init__(self, r, g, b):
        self._r = self._clamp(r)
        self._g = self._clamp(g)
        self._b = self._clamp(b)

    def get_rgb(self):
        return (self._r, self._g, self._b)

    def remove_red(self):
        self._r = 0

    def __str__(self):
        return "Color(" + str(self._r) + "," + str(self._g) + "," + str(self._b) + ")"

    def __eq__(self, other):
        if not isinstance(other, Color):
            return NotImplemented
        return self._r == other._r and self._g == other._g and self._b == other._b