# Palindrome - word that reads same backwards as forwards

def palindrome(word):
    if word == word[::-1]:
        print("Yes it is palindrome.")
    else:
        print("No ,it is not a palindrome.")
        
word = input("Enter the word:-")
palindrome(word)

