#Triangle classifier
# eqilatral -all side equal, isoscales -2 sides equal, scalene - no sode equale

a = float(input("Enter the side a :"))
b = float(input("Enter the side b :"))
c = float(input("Enter the side c :"))

if a == b == c:
    print("eqilatral")
elif a == b or b == c or c == a:
    print("isoscales")
else:
    print("scalene")
