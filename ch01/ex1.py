from random import randint

def guessing_game():
    return randint(0, 100)

number = guessing_game()
success = 0

while success == 0:
   user_guess = int(input("Try to guess the random number: "))

   if user_guess == number:
       print("Just right!")
       success = 1
   elif user_guess > number:
       print("Too high.")
   else:
       print("Too low.")
