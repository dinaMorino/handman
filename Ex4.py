class Hexagon():
    def __init__(self, w):
        self.width = w
    def perimeter(self):
        return self.width * 6
hex1 = Hexagon(3)
print(hex1.perimeter())
