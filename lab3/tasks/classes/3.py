class Shape:
    def Area(self):
        print("Area equals zero")

class Recatngle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def Area(self):
        S = self.length * self.width
        print(S)


x = Recatngle(int(input()), int(input()))
y = Shape()

y.Area()
x.Area()
