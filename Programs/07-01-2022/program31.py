from Graphics import rectangle,circle
from Graphics.Three_D_Graphics import cuboid,sphere
print("RECTANGLE")
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
print("The area of rectangle is:")
rectangle.area(l,b);
print("The perimeter of rectangle is:")
rectangle.perimeter(l,b);
print("CIRCLE")
r=int(input("Enter the radius:"))
print("The area of circle is:")
circle.area(r);
print("The perimeter of circle is:")
circle.perimeter(r);
print("CUBOID")
o=int(input("Enter the length:"))
p=int(input("Enter the breadth:"))
q=int(input("Enter the height:"))
print("The area of cuboid is:")
cuboid.area(o,p,q);
print("The perimeter of cuboid is:")
cuboid.perimeter(o,p,q);
print("SPHERE")
R=int(input("Enter the radius:"))
print("The area of Sphere is:")
sphere.area(R);
print("The perimeter of Sphere is:")
sphere.perimeter(R);