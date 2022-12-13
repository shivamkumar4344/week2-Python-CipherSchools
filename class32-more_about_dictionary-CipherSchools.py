# from keys
d = dict.fromkeys(range(1,11),'unknown')
print(d)

# get method

dic = {'name':'Shivam','age':22,'height':5.4}
print(dic.get('height'))

if dic.get('age'):
    print('present')
else:
    print('not present')
    
dic1 = dic.copy()
print(dic1)