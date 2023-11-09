import random

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

list1 = ['apple', 'ball', 'love', 'welcome']

choosen_word = random.choice(list1)

#print(choosen_word)

length_of_choosen_word = len(choosen_word)

dashes = []

for i in range(length_of_choosen_word):
    dashes += '_'
print(dashes)

Game_over = False

lives = 0

while not Game_over:
    user_guess = input("Guess a letter :")

    for i in range(length_of_choosen_word):

        letter = choosen_word[i]
        if letter == user_guess:
            dashes[i] = user_guess
            print(dashes)
    if user_guess not in choosen_word:
        lives += 1
        if lives == 6:
            Game_over = True
            print('you lose')
    if '_' not in dashes:
        Game_over = True
        print('you won')
    print(hangman[lives])

