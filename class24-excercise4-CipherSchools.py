# define a function which filters out odd and even

def filter_odd_even(n):
    odd = []
    even = []
    for i in n:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    out = [even,odd]
    return out
    
nums = [1,2,3,4,5,6,7,8,9,10]
print(filter_odd_even(nums))