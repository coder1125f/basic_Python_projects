import random
import emoji


emojiiz = {'r': emoji.emojize(':raised_fist:'), 'p': emoji.emojize(':raised_hand:'), 's': emoji.emojize(':victory_hand:')}
choices = ['r', 'p', 's']

def play():
    user = input('Rock Paper Scissors? (r / p / s) : ').lower()
    print(f'user {emojiiz[user]}')
    computer = random.choice(choices)
    print(f'computer {emojiiz[computer]}')

    winer(user, computer)

def winer(user, computer):
    status = ''
    if user == computer:
        status = 'draw'
    elif user == 'r':
        if computer == 'p':
            status = 'lose'
        elif computer == 's':
            status = 'win'
    elif user == 's':
        if computer == 'p':
            status = 'win'
        elif computer == 'r':
            status = 'lose'
    print(status)

play()
print()
while True:
    answer = input('Do you want to play again? (y/n) : ').lower()
    if answer == 'y':
        play()
        print()
    else:
        break