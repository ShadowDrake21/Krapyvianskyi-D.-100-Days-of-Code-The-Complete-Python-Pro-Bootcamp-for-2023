import random

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

moves = [rock, paper, scissors]
person_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if person_move >= 3:
    print("Invalid data. You lose")
    exit()
print(moves[person_move])

pc_move = random.randint(0, 2)
print("Computer chose:\n" + moves[pc_move])

if (person_move == 0 and pc_move == 2) or (person_move == 1 and pc_move == 0) or (person_move == 2 and pc_move == 1):
    print("You win!")
elif (person_move == 2 and pc_move == 0) or (person_move == 0 and pc_move == 1) or (person_move == 1 and pc_move == 2):
    print("You lose")
else:
    print("Draw!")
