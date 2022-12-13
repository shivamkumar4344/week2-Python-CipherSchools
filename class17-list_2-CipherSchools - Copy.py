#sort,count,sorted,reverse,clear,copy

numbers = [1,3,5,7,9,10]
numbers.sort()
print(numbers)

print(numbers.count(1))

print(sorted(numbers))

numbers_copy = numbers.copy()
print(numbers_copy)

numbers.clear()
print(numbers)


# is or equals
fruits1 = ['mango','kiwi','orange','apple']
fruits2 = ['strawberry','guava','pineapple']
fruits3 = ['mango','kiwi','orange','apple']
print(fruits1 == fruits2)
print(fruits1 == fruits3)
print(fruits1 is fruits3)

#join and split

name,age = input("Enter your name and age:-").split(',')
print(name)
print(age)


user_info =['shivam','20']
print(','.join(user_info))
