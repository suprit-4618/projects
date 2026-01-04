import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print("What do you choose? Type O for Rock, 1 for Paper, 2 for Scissors.")
game = [rock, paper, scissors]
user_input = int(input())
user = game[user_input]
computer = random.choice(game)
print(user)
print(computer)
if user == computer:
    print("Draw")
elif user == rock and computer == paper:
    print("Computer wins!")
elif user == rock and computer == scissors:
    print("User wins!")
elif user == paper and computer == rock:
    print("User wins!")
elif user == paper and computer == scissors:
    print("Computer wins!")
elif user == scissors and computer == paper:
    print("user wins!")
elif user == scissors and computer == rock:
    print("computer wins!")
