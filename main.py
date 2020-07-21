import random

gameover = False
while not gameover:
  computer_number = random.randint(1, 10)
  player_number = -1
  tries = 0
  while player_number != computer_number:
    player_number = int(input("Type your number here:"))
    tries += 1
    if computer_number == player_number:
      print(f"horray you guessed the correct number in {tries} tries")
    elif player_number > computer_number:
      print("too high")
    elif player_number < computer_number:
      print("too low")
      
  choice = input("play again Y/N:")
  if choice != "y":
    gameover = True