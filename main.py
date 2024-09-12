import random

# List of words to choose from
hangman_words = ["abruptly", "absurd", "avenue", "awkward", "buffalo", "crypt", "duplex", "equip",
                 "faking", "funny", "galaxy", "gossip", "icebox", "injury", "ivory", "jackpot", "ovary", "oxygen"]

# Select a random word
random_word = random.choice(hangman_words)

# A set to track guessed letters
guessed_letters = set()

# Number of attempts
attempts = len(random_word) + 2

# Replace each letter with an underscore
hidden_word = ["_" for _ in random_word]

print("Welcome to the Hangman game!!")
print(f"You have {attempts} attempts to guess the word.")
print(' '.join(hidden_word))  # Display hidden_word with spaces for better readability

while attempts > 0:
    user_input = input("Guess the letter: ").lower()

    # Ensure that user can only choose one letter at a time
    if len(user_input) != 1 or not user_input.isalpha():
        print("Invalid choice.")
        continue

    # Ensure that the user cannot choose letters that have been chosen before
    if user_input in guessed_letters:
        print(f"You have already chosen '{user_input}'. Try another letter.")
        continue

    # Add guessed letter to the set
    guessed_letters.add(user_input)

    # Determine if the letter is in the word
    if user_input in random_word:
        print(f"Good guess! '{user_input}' is in the word.")
        # Reveal the guessed letter in the hidden word
        for index, letter in enumerate(random_word):
            if letter == user_input:
                hidden_word[index] = user_input
    else:
        print(f"Sorry, '{user_input}' is not in the word.")
       
    # Show the current state of the hidden word and remaining attempts
    print(' '.join(hidden_word))  # Display the hidden_word with spaces for better readability
    print(f"Remaining attempts: {attempts}")
     # Reduce the number of attempts for an incorrect guess
    attempts -= 1  

    # Check if the user guessed all the correct letters
    if "_" not in hidden_word:
        print("Congratulations! You won the game.")
        break
else:
    print(f"Game over! You lost. The word was '{random_word}'.")
