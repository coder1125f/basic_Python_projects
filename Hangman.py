import random

def choose_word():
    words = ['apple', 'computer', 'scientist', 'teacher', 'robic', 'laptop']
    word = random.choice(words)
    return word

def hint(word):
    length = len(word)
    word_holder = ["_"] * length
    return word_holder

def show_hangman(wrong_guesses):
    hangman_list = {0: ("+---+  \n"
                        "|      \n"
                        "|      \n"
                        "|      \n"
                        "|__    "),

                    1: ("+---+  \n"
                        "|   o  \n"
                        "|      \n"
                        "|      \n"
                        "|__    "),

                    2: ("+---+  \n"
                        "|   o  \n"
                        "|   |  \n"
                        "|      \n"
                        "|__    "),

                    3: ("+---+  \n"
                        "|   o  \n"
                        "|  /|  \n"
                        "|      \n"
                        "|__    "),

                    4: ("+---+  \n"
                        "|   o  \n"
                        "|  /|\\\n"
                        "|      \n"
                        "|__    "),

                    5: ("+---+  \n"
                        "|   o  \n"
                        "|  /|\\\n"
                        "|  /   \n"
                        "|__    "),

                    6: ("+---+  \n"
                        "|   o  \n"
                        "|  /|\\\n"
                        "|  / \\\n"
                        "|__    ")}
    return hangman_list[wrong_guesses]

def main():

    word = choose_word()
    length = len(word)
    word_holder = hint(word)
    print(word_holder)
    wrong_guesses = 0

    while wrong_guesses < 6 or ("_" in word):
        guess = input("Guess a letter: ").lower()

        if guess == word:
            break

        if guess in word:
            print(f'all right, "{guess}" is in the word. 👍')
            for i in range(length):
                if word[i] == guess:
                    word_holder[i] = guess

        else:
            wrong_guesses += 1
            print(f"sorry! '{guess}' is not in the word. ❌'")

        if wrong_guesses == 6:
            break
        print(word_holder)

    if wrong_guesses >= 6:
        print("Sorry, you lose!")
        print(show_hangman(wrong_guesses))

    else:
        print("You win!")
        print(show_hangman(wrong_guesses))



print("Welcome to Hangman!\n")

playing = True
while playing:
    main()

    order = input("Would you like to play again? (y/n) ").lower()
    if order == "y":
        continue
    else:
        playing = False