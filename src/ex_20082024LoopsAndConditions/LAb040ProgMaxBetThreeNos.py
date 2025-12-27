# Program to find max between 3 nos
# Logic building
# inupt->no1,no2,no3
# O/p->int, string
# Logic ->if else if else
no1 = int(input("Enter first no: "))
no2 = int(input("Enter second no: "))
no3 = int(input("Enter third no: "))
"""if no1 > no2 and no1 > no3:
    print(f"Max no is  {no1}")
elif no2 > no1 and no2 > no3:
    print(f"Max no is  {no2}")
else:
    print(f"Max no is  {no3}")
"""
result = max(no1,no2,no3)
print(f"Max no is {result}")