#Write a program to Count Vowels in a String
text = input("Enter text: ")
vowels = "a,e,i,o,u"
count = 0
for char in text:
    if char in vowels:
        count +=1
print(f"total number of vowels = {count}")