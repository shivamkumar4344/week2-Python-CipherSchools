# Lists 
# It is used to used to more than one value in a single list.

list1=['mango','apple','orange','Guava']
list1.append('banana')
print(list1)

list1.pop()
print(list1)
list1.pop(2)#removes the no. which is passed
print(list1)

list1.remove('apple')
print(list1)

# checking if a particular element is present in list or not

fruits = ['orange','mango','kiwi','pear']
if 'mango' in fruits:
    print("Yes it is present")
else:
    print("No,it is not present")

