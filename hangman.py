import random

# List of 5 predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Randomly select a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_attempts = 6
wrong_guesses = 0

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

# Main game loop
while wrong_guesses < max_attempts:

    # Display the word with guessed letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the whole word has been guessed
    if "_" not in display_word:
        print("\nCongratulations!")
        print("You guessed the word:", word)
        break

    # Get a letter from the player
    guess = input("Enter a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the letter to guessed letters
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("Correct guess!")

    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Incorrect guesses:", wrong_guesses, "/", max_attempts)

# If player uses all attempts
if wrong_guesses == max_attempts:
    print("\nGame Over!")
    print("The correct word was:", word)

print("\nThanks for playing!")
