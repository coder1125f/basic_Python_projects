# balance
def show_balance(balance):
    return balance

# deposite
def deposit():
    amount = input("How much do you want to deposit? ")
    if not amount.isdigit():
        print("Please enter a number.")
        deposit()
    amount = float(amount)
    if amount < 0:
        print("Please enter a valid amount.")
        deposit()
    return amount

# withdraw
def withdraw():
    amount = input("How much do you want to withdraw? ")
    if not amount.isdigit():
        print("Please enter a number.")
        withdraw()
    amount = float(amount)
    if amount < 0:
        print("Please enter a valid amount.")
        withdraw()
    if amount > balance:
        print(f"You dont have ${amount} to withdraw.")
        withdraw()
    return amount

balance = 1000

print('****************************')
print('Welcome to bank acount app')

def show_questions():
    global balance

    print('Which operation would you like to do?')
    print('1: Showing your balance')
    print('2: Deposite')
    print('3: Withdraw')
    print('4: Exit')

    answer = input('>> ')

    if answer == '1':
        print(show_balance(balance))
    elif answer == '2':
        amount = deposit()
        balance = show_balance(balance) + amount
    elif answer == '3':
        amount = withdraw()
        balance = show_balance(balance) - amount

    else:
        print('Please enter a valid answer.')
        show_balance()

    return balance

balance = show_balance(balance)

show_questions()


next = input('Do you want to do anything else? (y / n): ').lower()
while next:
    if next == 'n':
        print('Have a nice day!')
        break

    show_questions()
    next = input('Do you want to do anything else? (y / n): ').lower()
