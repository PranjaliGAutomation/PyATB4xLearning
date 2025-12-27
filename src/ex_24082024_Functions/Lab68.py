# Create a program to get sum of 3 numbers as user input
from src.ex_17082024Literals.Lab033 import result

num1 = int(input("Enter the num1"))
num2 = int(input("Enter the num2"))
num3 = int(input("Enter the num3"))

def sum_of_three_nums(n1, n2, n3):
    return n1 + n2 + n3
result = sum_of_three_nums(num1, num2, num3)
print(result)

result = sum_of_three_nums(n1 = num1, n2 = num2, n3=num3)
print(result)