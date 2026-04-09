"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Vladimír Kadlec
email:  vladimir.kadlec@example.com
"""

import random


def generate_secret():
    """Generates a random 4-digit number with unique digits, not starting with 0."""
    digits = list("123456789")
    first = random.choice(digits)
    remaining = [d for d in "0123456789" if d != first]
    rest = random.sample(remaining, 3)
    return first + "".join(rest)


def validate_guess(guess):
    """Returns an error message string if the guess is invalid, or None if valid."""
    if not guess.isdigit():
        return "Please enter digits only."
    if len(guess) != 4:
        return "Please enter exactly 4 digits."
    if guess[0] == "0":
        return "The number must not start with zero."
    if len(set(guess)) != 4:
        return "All digits must be unique."
    return None


def evaluate(secret, guess):
    """Returns (bulls, cows) for the given guess against the secret."""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows


def format_result(bulls, cows):
    """Formats the bulls/cows result with correct singular/plural."""
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"
    return f"{bulls} {bull_word}, {cows} {cow_word}"


def print_intro():
    print("Hi there!")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)


def play():
    print_intro()
    secret = generate_secret()
    guesses = 0

    while True:
        guess = input("\nEnter a number:\n>>> ").strip()
        error = validate_guess(guess)
        if error:
            print(error)
            continue

        guesses += 1
        bulls, cows = evaluate(secret, guess)

        if bulls == 4:
            print(f"Correct, you've guessed the right number")
            print(f"in {guesses} {'guess' if guesses == 1 else 'guesses'}!")
            print()
            if guesses <= 5:
                print("That's amazing!")
            elif guesses <= 10:
                print("That's average.")
            else:
                print("That's a bit over average.")
            break

        print(format_result(bulls, cows))


if __name__ == "__main__":
    play()
