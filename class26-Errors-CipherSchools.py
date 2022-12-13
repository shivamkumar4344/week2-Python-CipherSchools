try:
    a=3/0
except Exception as e:
    print(e)
    
    
try:
    b =4/5
    c =b+2
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Every thing is fine")
finally:
    print("Cleaning  up...")
    

    