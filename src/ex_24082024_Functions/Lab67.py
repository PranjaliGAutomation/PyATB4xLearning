#Types of function
#1. They cant return anything
#no return type no parameter NRNP
def greet():
    print("Hello World")

result = greet()
print(result)

#2No return type with argument
def greet_by_name(name):
    print("Hello ", name)

greet_by_name("Pranjali")

#3 No return type with default Argument
def say_hello_to_default_arg(name= "pranjali"):
    print("HEllo", name.upper())

say_hello_to_default_arg() #default value will be passed
say_hello_to_default_arg("Manish")
say_hello_to_default_arg(name = "Danish")

#4. multiple args
def multiple_arg(name1 = "Prasnj", name2 = "Nil", name3 = "Sanya" ):
    print("Multile Args:", name1, name2, name3)

multiple_arg()
multiple_arg("Anuj" , "Shamal", "shinha")

#4. Argument and Retuntype
def sum_of_two_numbers(num1, num2):
    return num1 + num2
result1 = sum_of_two_numbers(10,45)
result = sum_of_two_numbers(900,100)
print(result1 , result)


