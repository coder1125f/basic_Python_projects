import random
import string

def generate_password(min_length, letters=True, special=True):
    characters = string.digits
    if letters:
        characters += string.ascii_letters
    if special:
        characters += string.punctuation

    psw = ''
    meets_criteria = False
    has_letters = False
    has_special = False
    while len(psw) < min_length or not meets_criteria:
        new_char = random.choice(characters)
        psw += new_char

        if new_char in string.ascii_letters:
            has_letters = True
        elif new_char in string.punctuation:
            has_special = True

        meets_criteria = True
        if letters:
            meets_criteria = has_letters
        if special:
            meets_criteria = meets_criteria and has_special

    return psw

min_length = int(input('Enter minimum length of password: '))
has_letters = input('Do you have letters? (y/n): ').lower() == 'y'
has_special = input('Do you have special characters? (y/n): ').lower() == 'y'
print(f'Your password: {generate_password(min_length, has_letters, has_special)}')