class Rectangle:
    def __init__(self, l, b):
        self.l1 = l
        self.b1 = b
    def area(self):
        area1 = self.l1 * self.b1
        return area1
    def perimeter(self):
        peri1 = 2*(self.l1 + self.b1)
        return peri1
    def compare(self, obj):
        if (self.area() == obj.area()):
            print("The areas of Rectangle1(", self.area(),") and Rectangle2(", obj.area(),") are equal")
        elif(self.area() > obj.area()):
            print("The areas of Rectangle1(", self.area(),") is greater than Rectangle2(", obj.area(),")")
        elif (self.area() < obj.area()):
            print("The areas of Rectangle1(", obj.area(), ") is greater than Rectangle2(", self.area(), ")")
        else:
            print("The areas are not equal")

print("RECTANGLE 1")
l = int(input("Enter the length of rectangle1:"))
b = int(input("Enter the breadth of rectangle1:"))
obj1 = Rectangle(l,b)
print("The area is:")
obj1.area();
print(obj1.area())
print("The perimeter is:")
obj1.perimeter();
print(obj1.perimeter())
print("RECTANGLE 2")
l=int(input("Enter the length of rectangle2:"))
b=int(input("Enter the breadth of rectangle3:"))
obj2 = Rectangle(l,b)
print("The area is:")
obj2.area();
print(obj2.area())
print("The perimeter is:")
obj2.perimeter();
print(obj2.perimeter())
print("Now Comparing The Rectangles")
obj1.compare(obj2)
