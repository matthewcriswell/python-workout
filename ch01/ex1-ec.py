from random import randint

def to_base(x, base):
    base_list = []
    while x > 0:
        if not x % base:
            x = int(x/base)
            base_list.append(0)
        else:
            remainder = int(x%base)
            if remainder == 10:
                base_list.append('A')
            elif remainder == 11:
                base_list.append('B')
            elif remainder == 12:
                base_list.append('C')
            elif remainder == 13:
                base_list.append('D')
            elif remainder == 14:
                base_list.append('E')
            elif remainder == 15:
                base_list.append('F')
            else:
                base_list.append(remainder)
            x = x - remainder
            x = int(x/base)
    base_list.reverse()
    return base_list

def guessing_game():
    return randint(0, 100)

def number_format():
    return randint(2,16)

def pretty_print(num):
    return ''.join(map(str,num))

raw_number = guessing_game()
num_base = number_format()
number = to_base(raw_number, num_base)
success = 0
tries = 0

print("The number guessing game.  You have 3 tries to guess a randomly generated number in a randomly generated number base.  We even tell you the number and the base.  Good luck!")
while success == 0:
   pretty_number = pretty_print(number)
   print(f"The number is: {pretty_number} in base {num_base}")
   user_guess_raw = int(input("Try to guess the random number: "))
   user_guess = to_base(user_guess_raw, num_base) 
   pretty_user_guess = pretty_print(user_guess)
   print(f"You guessed: {pretty_user_guess}")
   tries += 1
   if user_guess == number:
       print("Just right!")
       success = 1
   elif user_guess_raw > raw_number:
       print("Too high.")
   else:
       print("Too low.")
   if tries >= 3:
      print("Out of tries")
      break
   else:
      print("Tries left: ", 3-tries)






print("Now let's try a word guessing game.  Try to guess a word.")

from english_words import get_english_words_set
a_lot_of_words = list(get_english_words_set(['web2']))
less_words = []
for i in a_lot_of_words:
    if len(i) < 6:
        less_words.append(i)
less_words.sort()
print(len(less_words))

success = 0
tries = 0

from random import choice
the_word = choice(less_words)
the_word_index = less_words.index(the_word)
print(f"The word is: {the_word} which is element {the_word_index} in the list")

while success == 0:
   user_guess_raw = input("Try to guess the word: ")
   user_guess = user_guess_raw.lower()
   user_guess_index = less_words.index(user_guess)
   pretty_user_guess = user_guess

   print(f"You guessed: {pretty_user_guess} which is element {user_guess_index}")
   tries += 1

   if user_guess == the_word:
       print("Just right!")
       success = 1
   else:        
       if user_guess_index > the_word_index:
           print("The word is earlier in the dictionary.")
       else:
           print("The word is later in the dictionary.")
   if tries >= 3:
      print("Out of tries")
      break     
   else:    
      print("Tries left: ", 3-tries)
