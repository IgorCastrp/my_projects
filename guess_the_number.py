import random

total_guesses = 6
secret_number = random.randint(1, 20)

print('I\'m thinking in a number between 1 and 20 ("Type: use binary search))')

while total_guesses != 0:
    number_guessed = int(input('Try to guess the number: '))
    if number_guessed < secret_number:
        print('Too low')
    elif number_guessed > secret_number:
        print('Too high')
    else:
        print('I guessed, the number is: ', secret_number)
        break
    total_guesses -= 1
    print('Total guesses left: ', total_guesses)
if total_guesses == 0:
    print(f'Your guesses run out, you lost, my thinking number was: {secret_number}')
else:
    print('Bye bye')
print('\n')