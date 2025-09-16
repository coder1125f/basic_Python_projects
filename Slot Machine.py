import random

def spin():
    symbols = ['🍒', '🍕', '🎃', '😍', '💸']
    choices = random.choices(symbols, k=3)
    return choices

def show_items(rows):
    print(f'{rows[0]} | {rows[1]} | {rows[2]}')

def get_pay(rows):
    prizes = {'🍒': 3, '🍕': 7, '🎃': 5, '😍': 10, '💸':25}
    if rows[0] == rows[1] == rows[2]:
        pay = prizes[rows[0]] * 3
        return pay
    return 0


print("************************************")
print("Welcome to Python Slot Machine")
print("Symbols are: 🍒, 🍕, 🎃, 😍, 💸")
print("************************************")

def main():
    balance = 100

    while True:
        bet = input("How much would you like to bet? ")

        if not bet.isdigit():
            print("Please enter a number")
            bet = input("How much would you like to bet? ")

        bet = int(bet)
        if bet <= 0:
            print("Bet should be greater than zero.")
            bet = input("How much would you like to bet? ")

        balance -= bet
        choices = spin()
        print('Spinning...\n')

        show_items(choices)

        pay = get_pay(choices)
        if pay > 0:
            print(f'You win ${pay}')
        balance += pay

        print(f"Your balance is ${balance}")

        answer = input("Would you like to play again? (y/n): ").lower()
        if answer == 'y':
            choices
        elif answer == 'n':
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    main()