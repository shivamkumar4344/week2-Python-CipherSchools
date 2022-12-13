user_info  = {'name':'Shivam','age':20,'sec':'KOC27','roll':60}
del_item = user_info.pop('sec')
print(del_item)
print(user_info)


# update method
info = {'name':'Rakshit','age':20,'add':'Khagaul'}
more_info = {'name':'Shyam','State':'Bihar','hobbies':["Singing","Travelling","Reading Books"]}
info.update(more_info)
print(info)