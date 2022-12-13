n = int(input("Enter the number:-"))
total = 0
for i in range(1,n+1):
    total += i
print("Sum of n numbers=",total)

# calculate sum or digits ---->1+2+3+4

total = 0
num = input("Enter a no:-")
for i in range(0,len(num)):
    total+= int(num[i])
print("Add the digits=",total)

# Number of times the letter occurs

name   = input("Enter your name:-")
temp = ""
for i in range(0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp+=name[i]
        
#break
for i in range(1,11):
    if i == 5:
        break
    print(i)
    
# continue
for x in range(1,11):
    if x == 5:
        continue
    print(x)