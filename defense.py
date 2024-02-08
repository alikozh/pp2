class Shape:
    pass

class Circle(Shape):
    def __init__(self, rad):
        self.rad = rad
    
    def C(self):
        len_arc = 2 * 3.14 * self.rad
        print (f"the length of the arc {len_arc}")

circ = Circle(int(input()))
circ.C()
