#Write a program to calculate area of a circle
#area = pie*r^2
# input user float, pi= 3.14, power function or **
#O/p ->
import math

radius = float(input("Enter the radius of the circle: "))
#area = 3.14* pow(radius,2)
area=  math.pi*math.pow(radius,2)
print("Area of circle is :",area)
print("Area of circle is :",f"{area:.2f}")#After formatting