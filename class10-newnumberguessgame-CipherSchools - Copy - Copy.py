# Number guessing game
winner_num = 69
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