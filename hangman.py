import random

def play_hangman():
    words = ['python', 'programming', 'computer', 'algorithm', 'database', 'machine']
    word = random.choice(words).lower()
    letters = set(word)
    guessed_letters = set()
    guesses = 6
    
    while len(letters) > 0 and guesses > 0:
        print("You have {} guesses left.".format(guesses))
        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print(" ".join(word_list))
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in letters:
            letters.remove(guess)
            guessed_letters.add(guess)
        else:
            guesses -= 1
            
    if guesses == 0:
        print("Sorry, you lost. The word was {}.".format(word))
    else:
        print("Congratulations, you guessed the word {}!".format(word))

play_hangman()
