#Write a program that asks the user for their age and prints a message based on their input:

# If the user is under 18, print "You are a minor."
# If the user is 18 or older, print "You are an adult."

age= int(input("Enter your age  "))
if age>=18:
    print("You are an adult")
else:
    print("You are a minor")