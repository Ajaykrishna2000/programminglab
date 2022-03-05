tri_area = lambda b, h: 0.5 * (b * h)
rect_area = lambda l, r: l * r
sqr_area = lambda a: a * a
print("*****TRIANGLE*****")
b = int(input("Enter the base of triangle:"))
h = int(input("Enter the height of triangle:"))
print("Area of Triangle is:",tri_area(b, h))
print("*****RECTANGLE*****")
l = int(input("Enter the length of rectangle:"))
r = int(input("Enter the breadth of rectangle:"))
print("Area of Rectangle is:", rect_area(l, r))
print("*****SQUARE*****")
a = int(input("Enter the side of square:"))
print("Area of Square is:", sqr_area(a))