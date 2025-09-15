import random

colors = ['B', 'G', 'R',  'Y']

palette = random.choices(colors, k=4)
print(palette)

print(f'Guess palette of 4 colors: {colors}')

def play():
    guesses = 0
    while True:
        answer = [color.upper() for color in input("Enter your guess: ").split()]
        guesses += 1

        for i in answer:
            if i not in colors or len(answer) != 4:
                print(f'Please enter 4 valid colors.')
                continue

        if answer == palette:
            print(f'You got {guesses} guesses correct.')
            break

        correct_position = 0
        incorrect_position = 0


        temp = list(palette)
        for i in range(4):
            if answer[i] == palette[i]:
                correct_position += 1

            elif answer[i] in palette and answer[i] in temp:
                incorrect_position += 1
                temp.remove(answer[i])

        print(f'Correct Position: {correct_position} | Incorrect Position: {incorrect_position}')

        print(f'{5 - guesses} guesses remaining.')

        if guesses == 5:
            break

    return answer, guesses


print(play())
