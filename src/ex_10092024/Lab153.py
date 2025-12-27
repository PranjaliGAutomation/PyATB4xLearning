print("Start of the program")
Try:
a=int(input("Enter name"))
b=int(input("Enter name"))
c=a/b # 0 devision error, pranita -value error
print("Result",c)
except ValueError as ve:
print("you have entered string we wanr int")
except ZeroDevisionError as d
print("you have entered 0 we wanr int value")
else:
print(f"Result is {c}")
Finally:
print(Alwways executed)
print("End of the program")