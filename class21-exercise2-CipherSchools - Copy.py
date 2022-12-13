# define a function which takes 2 lists as input and return the element which contains the common in both list.
def common_finder(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output
print(common_finder([1,2,3,4,5],[2,4,6,8]))

