import random

def load_words(filename):
    """Load words from a file and return as a list."""
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words

def select_words(words, number_of_words):
    """Randomly select a specific number of words from the list."""
    return random.sample(words, min(number_of_words, len(words)))

def play_game(secret_words):
    """Play the guessing game with the selected secret words."""
    guesses = []
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while len(guesses) < len(secret_words) and not out_of_guesses:
        if guess_count < guess_limit:
            guess = input("Enter guess: ").strip()  # Remove any extra whitespace from the user's guess
            if guess in secret_words and guess not in guesses:
                guesses.append(guess)
                print(f"Good guess! You've guessed {len(guesses)} out of {len(secret_words)} words.")
            else:
                print("Incorrect guess or already guessed.")
            guess_count += 1
        else:
            out_of_guesses = True

    # Output the result
    if len(guesses) == len(secret_words):
        print("Congratulations! You guessed all the words!")
    else:
        print(f"Out of guesses! The correct words were: {', '.join(secret_words)}")

def main():
    filename = 'secretword.txt'
    all_words = load_words(filename)
    number_of_words = 3
    secret_words = select_words(all_words, number_of_words)
    play_game(secret_words)

if __name__ == "__main__":
    main()

