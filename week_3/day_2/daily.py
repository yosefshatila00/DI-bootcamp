import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self._radius = radius
        elif diameter is not None:
            self._radius = diameter / 2
        else:
            raise ValueError("Must specify radius or diameter")
    
    @property
    def radius(self):
        return self._radius
    
    @property
    def diameter(self):
        return self._radius * 2
    
    def area(self):
        return math.pi * self._radius ** 2
    
    def __str__(self):
        return f"Circle(radius={self._radius}, diameter={self.diameter}, area={self.area():.2f})"
    
    def __add__(self, other):
        return Circle(radius=self._radius + other._radius)
    
    def __lt__(self, other):
        return self._radius < other._radius
    
    def __eq__(self, other):
        return self._radius == other._radius

c1 = Circle(radius=5)
c2 = Circle(diameter=10)
c3 = Circle(radius=3)

print(c1)         
print(c2.radius)   
print(c3.diameter) 

c4 = c1 + c3
print(c4)         

print(c1 > c3)     
print(c1 == c2)    
circles = [c3, c1, c4, c2]
sorted_circles = sorted(circles)
for circle in sorted_circles:
    print(circle)
