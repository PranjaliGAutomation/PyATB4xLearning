"""FizzBuzz Test:
Write a program that prints numbers from 1 to 100. # Loop For
However, for multiples of 3, print "Fizz" instead of the number, and
for multiples of 5, print "Buzz."
For numbers that are multiples of both 3 and 5, print "FizzBuzz."""

for number in range(1, 100, 1):
    if (number % 3 == 0):
        print(f"{number} fizz")
    elif number % 5 == 0:
        print(f"{number} Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print(f"{number} fizzbuzz")
