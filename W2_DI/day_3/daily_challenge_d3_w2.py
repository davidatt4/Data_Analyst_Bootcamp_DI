import math

class Circle:
    def __init__(self,radius=None,diameter=None):
        if radius is not None:
            self.radius=radius
            self.diameter=radius*2
        elif diameter is not None:
            self.diameter=diameter
            self.radius=diameter/2
        else:
            raise ValueError("Please specify either radius or diameter")
    def area(self):
            return math.pi*(self.radius**2)

    def __str__(self):
        return f"Circle with radius: {self.radius}, diameter: {self.diameter}"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


circle1 = Circle(radius=3)
circle2 = Circle(diameter=10)
print(circle1.area())  
print(circle2)         
circle3 = circle1 + circle2
print(circle3)  
print(circle1 < circle2)  
print(circle1 == circle2)  
circles = [Circle(radius=5), Circle(radius=2), Circle(radius=8)]
sorted_circles = sorted(circles)
print(sorted_circles)  