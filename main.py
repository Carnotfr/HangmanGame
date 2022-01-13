import random
import time

# Initial steps to invite in the game:
print("\n Welcome to Hangman game")
name = input("Enter your name: ")
print("Hello " + name +  "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman")
time.sleep(3)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["January", "border", "image", "film", "promise", "kids", "lungs", "lungs", "doll","rhyme","damage","plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
    
#A loop to re-execute the game when the first round ends

def play_loop():
    global play_game
    play_game = input("Do you want to play again? y = yes, n = no \n")
    if play_game == "y"
        main()
    elif play_game == "n":
        print("Thanks for playing! We expect you back again!")
        exit()

# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input ("This is the Hangman word: " + display + "\nEnter your guess: \n")
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or