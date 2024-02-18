import random
import Hangman_ascii
import Hangman_words

chosen_word = random.choice(Hangman_words.words)
word = ["_" for _ in chosen_word]  

end_game = False
lives = 6
while not end_game and lives >= 0:
    print(word)  
    guess = input("Guess a letter: ").lower()
    if guess in word:
        print(f"You have already guessed {guess}.")

    if guess in chosen_word:  
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                word[i] = guess  
    else:
        print(Hangman_ascii.HANGMANPICS[6 - lives])  
        print("Sorry, your guess is wrong. You lose a life.")
        lives -= 1

    if "_" not in word: 
        print("Congratulations! You guessed the word correctly!")
        end_game = True

if lives == -1:
    print("Sorry, you lose! The word was:", chosen_word)
