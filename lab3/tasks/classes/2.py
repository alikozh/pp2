class Shape:
    def Area(self):
        print("Area equals zero")

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def Area(self):
        S = self.length * self.length
        print(S)


x = Square(int(input()))
y = Shape()

y.Area()
x.Area()
