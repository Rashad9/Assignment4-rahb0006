import random

def hangman():
    words = ['python', 'docker', 'hangman', 'developer']
    word = random.choice(words)
    guessed = "_" * len(word)
    attempts = 7
    guessed_letters = set()

    print("Welcome to Hangman!")
    print(f"Word to guess: {guessed}")

    while attempts > 0 and "_" in guessed:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            guessed = "".join([guess if letter == guess else guessed[i] for i, letter in enumerate(word)])
            print(f"Correct! Word now: {guessed}")
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts remaining.")

    if "_" not in guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over. The word was: {word}")

if __name__ == "__main__":
    hangman()
