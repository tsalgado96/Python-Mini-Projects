import random
from os import system, name

# Function to clear the terminal after every guess
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

# print('|-----')
# print('|    |')
# print('|    O')
# print('|   /|\\')
# print('|    |')
# print('|   / \\')

# 21 Possible Words
possible_words = (['Arctic', 'Blanket', 'Blizzard', 'Chilly', 'Coat', 'December', 'Fireplace', 'Freezing', 'Frozen', 'Furnace', 'Gloves', 'Hibernate', 'Radiator', 'Reindeer', 'Skates', 'Snow', 'Snowball', 'Snowman', 'Windy', 'Winter', 'Turtleneck'])
correct_word = possible_words[random.randint(0,20)].upper()
correct_word_list = []
length_of_word = len(correct_word)
display = '_' * length_of_word
display_list = []
letters_guessed = []
guess_right = False
number_of_guesses = 0
hangman = ['|-----', 
           '|    |', 
           '|     ', 
           '|       ', 
           '|     ', 
           '|       ', 
           '\n']

# Convert word into a list
for letter in correct_word:
    correct_word_list.append(' ')
    correct_word_list.append(letter)

# Convert display into a list
for letter in display:
    display_list.append(' ')
    display_list.append('_')

while not(guess_right): 
    #print(correct_word)
    if number_of_guesses != 6:
        if '_' in display_list:
            print('Letters guessed: ', *letters_guessed)
            print(*hangman, sep='\n')
            print(''.join(display_list) + '\n')
            user_input = input('Guess the word or a letter: ').upper()
            print('\n')
            if user_input >= 'A' and user_input <= 'Z':
                if len(user_input) == 1 or user_input == correct_word:
                    if user_input in letters_guessed:
                        clear()
                        print('You have already guessed that letter.')
                    else:
                        if user_input == correct_word:
                            clear()
                            print('Letters guessed: ', *letters_guessed)
                            print(*hangman, sep='\n')
                            print(*correct_word_list, sep='')
                            print('You Win!!! (By guessing the correct word)')
                            guess_right = True
                        elif user_input in correct_word:
                            clear()
                            letters_guessed.append(user_input)
                            count = len(correct_word_list) - 1
                            while count > 0:
                                if user_input == correct_word_list[count]:
                                    display_list[count] = user_input
                                    count -= 1
                                else:
                                    count -= 1
                        elif user_input not in correct_word:
                            clear()
                            number_of_guesses += 1
                            letters_guessed.append(user_input)
                            if number_of_guesses == 1:
                                hangman[2] = '|    O'
                            elif number_of_guesses == 2:
                                hangman[3] = '|    |'
                                hangman[4] = '|    |'
                            elif number_of_guesses == 3:
                                hangman[3] = '|   /|'
                            elif number_of_guesses == 4:
                                hangman[3] = '|   /|\\'
                            elif number_of_guesses == 5:
                                hangman[5] = '|   / '
                            elif number_of_guesses == 6:
                                hangman[5] = '|   / \\'
                            # elif number_of_guesses == 7:
                                
                else:
                    clear()
                    print('Not a valid input.')
            else:
                clear()
                print('Not a valid input.')
        elif '_' not in display_list:
            print('Letters guessed: ', *letters_guessed)
            print(*hangman, sep='\n')
            print(''.join(display_list) + '\n')
            guess_right = True
            print('You Win!!!')
        
    elif number_of_guesses == 6:
        print('Letters guessed: ', *letters_guessed)
        print(*hangman, sep='\n')
        print('The word was: ' + correct_word)
        print('YOU LOSE!!!')
        guess_right = True
