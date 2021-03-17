import random
import string

print("H A N G M A N")

while True:
    user_choice = input('Type "play" to play the game, "exit" to quit:')

    if user_choice == 'play':
        print()

        languages = ['python', 'java', 'kotlin', 'javascript']
        word = random.choice(languages)
        pattern = list(word)
        current_try = 0
        tries = 8
        literal = 0
        entered = []

        while literal < len(pattern):
            pattern[literal] = '-'
            literal += 1

        while current_try <= tries:

            if '-' not in pattern:
                current_try = 10
                print(word)
                print('You guessed the word!')
                print('You survived!')
                break

            print(''.join(pattern))
            user_input = input('Input a letter:')

            conditions = {
                0: word.find(user_input) != -1,                              # User letter is in the word
                1: user_input != '',                                         # User letter is not an empty character
                2: user_input not in entered,
                3: user_input in string.ascii_lowercase,
                4: len(user_input) == 1,                                     # User passed a single character
                5: user_input in word,
            }

            if (conditions[0] and conditions[1] and conditions[2] and conditions[3]) is True:
                pattern[int(word.find(user_input))] = word[int(word.find(user_input))]
                pattern[int(word.rfind(user_input))] = word[int(word.rfind(user_input))]

            elif conditions[4] is False:
                print("You should input a single letter")

            elif conditions[2] is False:
                print("You've already guessed this letter")

            elif conditions[3] is False:
                print("Please enter a lowercase English letter")

            elif (conditions[5] and conditions[2]) is False:
                print("That letter doesn't appear in the word")
                current_try += 1
            entered.append(user_input)

            if current_try == tries:
                print("You lost!")
                break

            print()

    elif user_choice == 'exit':
        exit()