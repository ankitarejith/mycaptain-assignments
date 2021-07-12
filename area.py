#Program to calculate the Area of a circle

from math import pi
radius=float(input("Enter the value of the radius:"))

area=pi*radius*radius

print("The area of the circle is:",format(area,'.3f'),"sq units")
