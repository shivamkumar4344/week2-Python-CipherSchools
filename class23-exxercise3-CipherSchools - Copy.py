#reverse the elements in the list
def reverse_words(l):
    elements=[]
    for i in l:
        elements.append(i[::-1])
    return elements
words = ['abc','def','ghi']
print(reverse_words(words))