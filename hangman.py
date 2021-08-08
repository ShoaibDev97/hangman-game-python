#imports libraries and files
import random
from word_list import word_list
from stages import stages,logo

# Declaring Variables
guess_word = random.choice(word_list).lower()
word_len = len(guess_word)
lives = 6
end_of_game = False
dash = []

print(logo,end="\n \n")

# Make Sure To Remove this Line 
print(f"Cheating Word will be {guess_word}")

# generating Dash 
for _ in range(word_len):
    dash.append("_")


while end_of_game == False:
    guess_letter = input("Enter Guess Letter : ")

    if guess_letter in dash:
        print(f"Letter {guess_letter} is already been guessed.")
    

    for letter in range(word_len):
        if guess_letter == guess_word[letter]:
            dash[letter] = guess_letter 

    if guess_letter not in guess_word:
        lives -= 1
        print(stages[lives])
        print(f"Total Remaining Lives : {lives}")
        
        if lives == 0:
            print(f"You Loss the Game The Corrent Answer was : {guess_word}")
            end_of_game = True
            break
    if "_" not in dash:
        print("congratualation you won the game")
        break
    
    print(dash)
