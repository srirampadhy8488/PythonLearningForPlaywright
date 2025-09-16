#Create a program that takes two numbers as input and prints which one is greater, or if they are equal.
num1= int(input("Enter first number   "))
num2= int(input("Enter second number   "))

if num1==num2:
    print("Both numbers are equal")
elif num1>num2:
    print("num1 is greater")
else:
    print("num2 is greater")