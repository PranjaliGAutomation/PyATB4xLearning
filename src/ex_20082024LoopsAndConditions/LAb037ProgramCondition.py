# Write a program if you are allowed to go to club or not
# Logic building,input->int,O/p->if user can go or not
# if age>21 can go , else not go
age = int(input("Enter your age: "))
if age >= 21:
    print(f"You can go to club at {age}")
else:
    print(f"You can not go the club {age}")
