import random
import sys

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'


def get_computer_choice():
    return random.choice([ROCK, PAPER, SCISSORS])


def print_results(player_choice, computer_choice):
    if player_choice == computer_choice:
        print(f'You both chose {player_choice}. I\'s a Tie.')
    elif (player_choice == ROCK and computer_choice == SCISSORS) or \
         (player_choice == SCISSORS and computer_choice == PAPER) or \
         (player_choice == PAPER and computer_choice == ROCK):
        print(f'You choose {player_choice} and the computer choose {computer_choice}. You win!')
        return 'win'
    else:
        print(f'You choose {player_choice} and the computer choose {computer_choice}. You loss!')
        return 'loss'


def transform_player_input(player_choice):
    choices = {'1': 'rock', '2': 'paper', '3': 'scissors', '4': 'quit'}
    if player_choice in choices:
        return choices[player_choice]
    else:
        raise ValueError("Invalid input. Please choose a valid number: 1, 2, 3, or 4")


def main():

    total_wins = 0
    total_losses = 0
    total_ties = 0
    final_score = 0

    while True:
        try:
            player_choice_the_number = input("Choose the number: 1. rock, 2. paper, 3. scissors or 4. quit: ")
            player_choice = transform_player_input(player_choice_the_number)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if player_choice not in [ROCK, SCISSORS, PAPER, 'quit']:
            continue

        if player_choice == 'quit':
            print(f'\nI\'ve quit the game.\nTotal wins: {total_wins}, Total loss: {total_losses}, Total ties: {total_ties}'
                  f' = Total Score: {final_score}\n')
            sys.exit()

        computer_choice = get_computer_choice()
        results = print_results(player_choice, computer_choice)

        if results == 'win':
            total_wins += 1
            final_score += 1
        elif results == 'loss':
            total_losses += 1
            final_score -= 1
        else:
            total_ties += 1

        print(f'Total wins: {total_wins}, Total loss: {total_losses}, Total ties: {total_ties}'
              f' = Total Score: {final_score}\n')


if __name__ == '__main__':
    main()
