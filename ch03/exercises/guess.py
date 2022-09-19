import random

num = random.randrange(1,11)
num_guesses = 1

for i in range(3):
  guess_number = int(input("Enter a number:"))
  num_guesses += 1 
  if guess_number > num:
    print("The number you guessed was too high!")
  elif guess_number < num:
    print("The number you guessed was too low!")
  else:
    print("Correct!")
    correct_guess = True
    for i in range(3):
      if guess_number == num:
        break 
    print("Congrats! You guessed the number on your first try!")

print("It took you", num_guesses, "to get it correct!")