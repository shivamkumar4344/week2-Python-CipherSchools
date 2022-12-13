# Define Function
def add_two(a,b):
    return a+b
a = float(input("Enter the first number:-"))
b = float(input("Enter the second number:-"))
print(add_two(a,b))

# Function for odd and even
def odd_even(num):
    if num%2  ==0:
        return 'even'
    return 'odd'
print(odd_even(100))

def is_odd(num):
    return num%2 != 0

print(is_odd(10))


