# VERSION 1.0

# Ask for player input 
# Generate random computer input
# Run it against if loop

# import random

# player_turn = input("What is your move? ")
# computer_turn = random.randint(1,3)
# if computer_turn == 1:
#     computer_turn = 'rock'
# elif computer_turn == 2:
#     computer_turn = 'paper'
# elif computer_turn == 3:
#     computer_turn = 'scissors'
# print(f'The CPU chose {computer_turn}')
# player_turn = player_turn.lower().strip()
# if player_turn == computer_turn:
#     print('Tie!')

# if player_turn == 'rock':
#     if computer_turn == 'scissors':
#         print('You win!')
#     else:
#         print('CPU wins!')
# if player_turn == 'scissors':
#     if computer_turn == 'rock':
#         print('CPU wins!')
#     else:
#         print('You win!')
# if player_turn == 'paper':
#     if computer_turn == 'rock':
#         print('CPU wins!')
#     else:
#         print('You win!')

# VERSION 1.1
# Added a game loop that asks if you want to play again

import random

answer = 0
while answer != 'q':
    player_turn = input("What is your move? ")
    if player_turn == 'q':
        break
    computer_turn = random.randint(1,3)
    if computer_turn == 1:
        computer_turn = 'rock'
    elif computer_turn == 2:
        computer_turn = 'paper'
    elif computer_turn == 3:
        computer_turn = 'scissors'
    print(f'The CPU chose {computer_turn}')
    player_turn = player_turn.lower().strip()
    
    if player_turn == computer_turn:
        print('Tie!')
        break
    
    if player_turn == 'rock':
        if computer_turn == 'scissors':
            print('You win!')
        else:
            print('CPU wins!')
    if player_turn == 'scissors':
        if computer_turn == 'rock':
            print('CPU wins!')
        else:
            print('You win!')
    if player_turn == 'paper':
        if computer_turn == 'rock':
            print('CPU wins!')
        else:
            print('You win!')
