# import the words form words
from words import words

# import random module
import random

# to add space from the top
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

# randomly take a word from words
rand_words = random.choice(words)

# creating the guess word
word = rand_words

# creating basic variables
guesses = [word[-1]]
errors = 6
done = False

# until done is not true
while not done:

    # if the letter is in guesses
    for letter in word:
        if letter in guesses:
            print(letter, end = '  ')
        else:
            print('_', end = '  ')

    # asking the guess letter from the user
    guess = input(f'\n\nAllowed errors: {errors} Enter your guess: ')
    print('\n')
    guesses.append(guess)

    # if the guess is not in word then reduce the point
    if guess not in word:
        errors -= 1
        if errors == 0:
            break

    # set done to true
    done = True

    # if the letter is not in guesses then loop again
    for letter in word:
        if letter not in guesses:
            done = False

# giving the ending statement of the code
if done:
    print('You won the game!\n')
else:
    print(f'You lost! The word was {word}\n')