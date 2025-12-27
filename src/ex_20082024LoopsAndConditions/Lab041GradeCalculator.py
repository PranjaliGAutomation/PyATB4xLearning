# Write a program that calculatesand displays the letter grade for a given numerical,score
# A- 90-100
# B-80-89
# C-70-79#LOGIC BUILDING
# user input score- int, O/p->str A,B,C
score = int(input("Enter your marks/score: "))
if score >= 90 and score <=100:     # 90<= score <=90 Simplied chaining format
    print("Grade A ")
elif score >= 80 and score < 89:    #80<=score <=89
    print(f"Grade B ")
elif score >= 70 and score < 79:
    print(f"Grade C ")
elif 60 <= score < 69:
    print(f"Grade D ")
else:
    print("Grade f")
