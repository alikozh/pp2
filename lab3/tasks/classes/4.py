import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)
        
    def move(self, x1, y1):
        self.x += x1
        self.y += y1

    def dist(self):
        d = math.sqrt(self.x ** 2 + self.y ** 2)
        print(d)


p = Point(int(input()), int(input()))

p.show()

p.move(int(input()), int(input()))

p.show()

p.dist()


