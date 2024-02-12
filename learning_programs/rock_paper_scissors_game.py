import random, sys

total_wins = 0
total_loss = 0
total_ties = 0
computer_choices = ['r', 'p', 's']

while True:

    computer_chose = random.choice(computer_choices)
    player_chose = input("Choose: (r)ock, (p)aper, (s)cissors or (q)uit: ").lower()

    if player_chose == 'r':
        if computer_chose == 'r':
            print(f'Computer randomly chose rock, tie')
            total_ties += 1
        elif computer_chose == 'p':
            print(f'Computer randomly chose paper, you lost')
            total_loss += 1
        else:
            print(f'Computer randomly chose scissors, you win')
            total_wins += 1

    elif player_chose == 'p':
        if computer_chose == 'r':
            print(f'Computer randomly chose rock, you win')
            total_wins += 1
        elif computer_chose == 'p':
            print(f'Computer randomly chose paper, tie')
            total_ties += 1
        else:
            print(f'Computer randomly chose scissors, you lost')
            total_loss += 1

    elif player_chose == 's':
        if computer_chose == 'r':
            print(f'Computer randomly chose rock, you lost')
            total_loss += 1
        elif computer_chose == 'p':
            print(f'Computer randomly chose paper, you win')
            total_wins += 1
        else:
            print(f'Computer randomly chose scissors, tie')
            total_ties += 1

    elif player_chose == 'q':
        print(f'\nTotal wins: {total_wins}, Total loss: {total_loss}, Total ties: {total_ties}')
        sys.exit()
    else:
        print('Choose a valid letter: r, p, s or q')


