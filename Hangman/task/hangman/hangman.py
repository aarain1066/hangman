import random
import sys

word_choices = ['python', 'java', 'kotlin', 'javascript']
rando_word = random.choice(word_choices)
blanks = list("-" * len(rando_word))
user_attempts = 8
user_letter_bank = set()
begin_game = None


def begin():
    print('Type "play" to play the game, "exit" to quit: ')
    global begin_game
    begin_game = input().lower()
    if begin_game == "exit":
        sys.exit()


print("H A N G M A N")

while begin_game != "play" and begin_game != "exit":
    begin()

while user_attempts != 0:
    print()
    print(''.join(blanks))
    if ''.join(blanks) == rando_word:
        print("You guessed the word!\n"
              "You survived!")
        break
    user_letter = input("Input a letter: ")
    if len(user_letter) > 1:
        print("You should input a single letter")
        continue
    elif user_letter.islower() is not True:
        print("Please enter a lowercase English letter")
        continue
    if user_letter not in user_letter_bank:
        user_letter_bank.add(user_letter)
    else:
        print("You've already guessed this letter")
        continue
    if user_letter not in rando_word:
        print("That letter doesn't appear in the word")
        user_attempts -= 1
        continue
    if user_letter in rando_word:
        for i in range(0, len(rando_word)):
            if user_letter == rando_word[i]:
                blanks[i] = user_letter
    else:
        print("Error")
else:
    print("You lost!")
