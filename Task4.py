"""Task is 
Implement a class Shape with method area().Create a subclass circle and Rectangle that implements the area method differently"""



class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = 3.14159 
        return pi * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
circle = Circle(5)
rectangle = Rectangle(4, 6)
print("Circle area:", circle.area())
print("Rectangle area:", rectangle.area())

"""Output is
Circle area: 78.53975
Rectangle area: 24
"""