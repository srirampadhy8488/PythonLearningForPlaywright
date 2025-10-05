#Write a program that prints the multiplication table for a given number up to 10.
number = int(input("Enter a number : "))
for i in range(1,11):
    result= number*i
    print(f"{number}*{i}={result}")