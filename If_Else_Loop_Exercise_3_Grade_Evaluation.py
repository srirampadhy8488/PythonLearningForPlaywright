#Write a program that asks for a student's score and prints the corresponding grade:

#90 and above: "A"
#80 to 89: "B"
#70 to 79: "C"
#60 to 69: "D"
#Below 60: "F"

score= float(input("Enter students score   "))
if score>=90:
    print("Grade is A")
elif score>=80:
    print("Grade is B")
elif score>=70:
    print("Grade is C")
elif score>=60:
    print("Grade is D")
else:
    print("Grade is F")