numbers = list(range(1,11))
print(numbers)

print(numbers.index(7))

def negative_list(l):
    negative = []
    for i in l:
        
        negative.append(-i)
    return negative
print(negative_list(numbers))
        
    
def square_list(n):
    square = []
    for i in n:
        square.append(i*i)
    return square

numbers = list(range(1,11))
print(square_list(numbers))