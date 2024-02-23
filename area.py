import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Instantiate the Circle class
circle_object = Circle(5)

# Calculate area and perimeter
area = circle_object.area()
perimeter = circle_object.perimeter()

# Print the results
print(f"The area of the circle with radius {circle_object.radius} is {area:.2f}")
print(f"The perimeter of the circle with radius {circle_object.radius} is {perimeter:.2f}")
    