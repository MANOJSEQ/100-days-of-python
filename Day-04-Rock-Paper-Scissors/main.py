rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game_images = [rock,paper, scissors]
options = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if options >=0 and options <=2:
    print(game_images[options])

computer_turn = random.randint(0,2)
print(f"Computer chose:")
print(game_images[computer_turn])

if options >= 3 or options<0:
    print("You have typed an invalid number. You lose")
elif options == 0 and computer_turn == 2:
    print("You win")
elif computer_turn == 0 and options == 2:
    print("You lose")
elif computer_turn > options:
    print("You lose")
elif options > computer_turn:
    print("You win")
elif computer_turn == options:
    print("Its a draw")


