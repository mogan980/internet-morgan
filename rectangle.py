import math
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return (self.length+self.width)*2
rectangle_object=Rectangle(6,5)
area=rectangle_object.area()
perimeter=rectangle_object.perimeter()
print(f"the area of the rectangle with length{rectangle_object.length}and width{rectangle_object.width}is{area}")
print(f"the perimeter of the rectangle with length{rectangle_object.length}and width{rectangle_object.width}is{perimeter}")