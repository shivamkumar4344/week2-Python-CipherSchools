def greatest(a,b):
    if a>b:
        return a
    else:
        return b

num1 = int(input("Enter the first number:-"))
num2 = int(input("Enter the second number:-"))
bigger = greatest(num1,num2)

print(f"{bigger} is greatest")

# Larger among three
def great_of_three(a,b,c):
    if a >b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
print(great_of_three(10,34,98))