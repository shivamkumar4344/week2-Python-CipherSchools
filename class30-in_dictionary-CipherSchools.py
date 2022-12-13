# checking if value is present or not in dictionary
user_info  = {'name':'Shivam','age':20}
if 'name' in user_info: # checking keys are present or not
    print("Present")
else:
    print("not present")
    
if 20 in user_info.values(): # cecking values are present or not
    print("present")
else:
    print('not present')


# loops in dictionary

for i in user_info:
    print(i)
    
for i in user_info.values():
    print(i)
    
items = user_info.items()
print(user_info)

for key,value in user_info.items():
    print(f" key is {key} and value is {value}")

