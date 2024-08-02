import requests


def guess_word():
    # Define the API endpoint
    url = "https://random-word-api.herokuapp.com/word?number=1"

    try:
        # Make the API request
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()

        # Get the random word from the response
        random_word = response.json()[0]

        return random_word

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


def check_guess(guess, word, correct_guesses):
    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                correct_guesses[index] = guess
        return True
    else:
        return False


# Main game logic
word_to_guess = guess_word()
if word_to_guess:
    correct_guesses = ['_'] * len(word_to_guess)
    lengthOfWord = len(word_to_guess)
    attempts_left = lengthOfWord  # You can set the number of attempts

    while attempts_left > 0 and '_' in correct_guesses:
        print("Word to guess: ", " ".join(correct_guesses))
        guessed_letter = input("Guess a letter: ").lower()

        if check_guess(guessed_letter, word_to_guess, correct_guesses):
            print("Good guess!")
        else:
            attempts_left -= 1
            print(f"Wrong guess. Attempts left: {attempts_left}")

        print("Current state of word:", " ".join(correct_guesses))

    if '_' not in correct_guesses:
        print("Congratulations! You've guessed the word:", word_to_guess)
    else:
        print("Sorry, you've run out of attempts. The word was:", word_to_guess)
else:
    print("Failed to get a word to guess.")
