x = int(input("Enter a number to check: "))
def even_odd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"
result = even_odd(x)
print(result)
#print(f"number {x} is {even_odd(x)}")