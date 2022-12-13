#  Modified Number guessing game
import random
winner_num = random.randint(1,100) # using random module to genrate random numbers
guess = 1
guess_num = int(input("Guess a number between 1 and 100 :"))
game_over = False

while not game_over:
    if guess_num == winner_num:
        print(f"You win , and you guessed this number in {guess} times.")
        game_over = True
    else:
        if guess_num < winner_num:
            print("too low")
            
        else:
            print("too high")
        guess+=1
        guess_num = int(input("Guess again:-"))
        
# New method for addding digits
num = input("Enter the number:")
total = 0
for i in num:
    total+=int(i)
print("On adding digits=",total)
        
