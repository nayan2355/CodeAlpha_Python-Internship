import random
words = ["python", "codealpha", "intern", "laptop", "hangman"]
word = random.choice(words)
guessed = ["_"] * len(word)
tries = 6
print("Welcome to Hangman!")
while tries > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed), f"| Tries left: {tries}")
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess: guessed[i] = guess
        print("Correct!")
    else:
        tries -= 1
        print("Wrong!")
if "_" not in guessed:
    print(f"You Win! Word was: {word}")
else:
    print(f"Game Over! Word was: {word}")