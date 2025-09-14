import random

print("Choose a number between 1 and 100")


def guess_number():
    low = 1
    high = 100
    attempts = 0

    while True:
        guess = random.randint(low, high)

        answer = input(f'Computer guessed {guess} ; if it correct, low or high? (c / l / h): ').lower() in ('c', 'l', 'h')



        attempts += 1
        if answer == 'c':
                break
        elif answer == 'l':
                low = guess + 1
        elif answer == 'h':
                high = guess - 1

    return guess, attempts

guess, attempts = guess_number()
print(f'computer guessed {guess} with {attempts} attempts')


