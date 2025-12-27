"""Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle."""

side_1 = int(input("Enter the 1st side :"))
side_2 = int(input("Enter the 2nd side :"))
side_3 = int(input("Enter the 3rd side :"))
if (side_1 == side_2 == side_3):
    print("it is an equilateral Triangle")
elif (side_1 == side_2 != side_3):
    print("it is an isosceles Triangle")
else:
    print("it is an scalene Triangle")
