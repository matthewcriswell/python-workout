from random import randint

def dec(x):
    return x

def guessing_game():
    return randint(0, 100)

def number_format():
    num_fmt = randint(0,3)
    if num_fmt == 0:
        return bin
    if num_fmt == 1:
        return oct
    if num_fmt == 2:
        return dec
    if num_fmt == 3:
        return hex

number = guessing_game()
success = 0
tries = 0

num_fmt = number_format()

while success == 0:
   user_guess = int(input("Try to guess the random number: "))
   tries += 1
   if user_guess == number:
       print("Just right!")
       success = 1
   elif user_guess > number:
       print("Too high.")
   else:
       print("Too low.")
   if tries >= 3:
      print("Out of tries")
      break
   else:
      print("Tries left: ", 3-tries)
