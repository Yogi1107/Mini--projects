import random

game_list = ['rock','paper','scissors']
machine_turn = random.choice(game_list)
user_input = input("Enter your turn (rock, paper or scissors): ")
if user_input == 'rock':
    if machine_turn =='rock':
        print(f"Machine Turn :{machine_turn}")
        print("Its a tie!!")
    elif machine_turn == 'paper':
        print(f"Machine Turn :{machine_turn}")
        print("You lose!")
    elif machine_turn == 'scissors':
        print(f"Machine Turn :{machine_turn}")
        print("You win!")
if user_input == 'paper':
    if machine_turn =='rock':
        print(f"Machine Turn :{machine_turn}")
        print("You win!!")
    elif machine_turn == 'paper':
        print(f"Machine Turn :{machine_turn}")
        print("Its a tie!")
    elif machine_turn == 'scissors':
        print(f"Machine Turn :{machine_turn}")
        print("You Lose!")
if user_input == 'scissors':
    if machine_turn =='rock':
        print(f"Machine Turn :{machine_turn}")
        print("You lose!!")
    elif machine_turn == 'paper':
        print(f"Machine Turn :{machine_turn}")
        print("You Win!")
    elif machine_turn == 'scissors':
        print(f"Machine Turn :{machine_turn}")
        print("Its a tie!")

#MODIFIED CODE
# import random

# game_list = ['rock', 'paper', 'scissors']
# machine_turn = random.choice(game_list)
# user_input = input("Enter your turn (rock, paper or scissors): ").lower()

# if user_input not in game_list:
#     print("Invalid input! Please enter rock, paper, or scissors.")
# else:
#     print(f"Machine Turn: {machine_turn}")

#     if user_input == machine_turn:
#         print("It's a tie!")
#     elif (
#         (user_input == 'rock' and machine_turn == 'scissors') or
#         (user_input == 'paper' and machine_turn == 'rock') or
#         (user_input == 'scissors' and machine_turn == 'paper')
#     ):
#         print("You win!")
#     else:
#         print("You lose!")

