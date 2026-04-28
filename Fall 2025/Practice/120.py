class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_from_origin(self):
        distance = ((self.x - 0)**2 + (self.y - 0)**2)**0.5
        return distance