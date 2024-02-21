import math

def area_polygon(n, a):
    A = (n * a**2) / (4 * math.tan(math.pi / n) )
    A = int(A)
    print(f"The area of the polygon is: {A}")

area_polygon(int(input()), int(input()))
