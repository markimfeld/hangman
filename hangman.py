import random

HANGMAN_PICS = [
    '''
    +---+
        |
        |
        |
       ===    
    ''',
     '''
    +---+
    O   |
        |
        |
       ===    
    ''',
    '''
    +---+
    O   |
    |   |
        |
       ===
    ''',
    '''
    +---+
    O   |
   /|   |
        |
       ===
    ''',
    '''
    +---+
    O   |
   /|\  |
        |
       ===
    ''',
    '''
    +---+
    O   |
   /|\  |
   /    |
       ===
    ''',
    '''
    +---+
    O   |
   /|\  |
   / \  |
       ===
    ''',
]

WORDS = [
    'cat',
    'dog',
    'car',
    'money',
    'java',
    'sql',
    'django'
]

def getSecretWord():
    secretWord = random.choice(WORDS)
    return secretWord

def showBlank(missedLetters, correctLetters, secretWord):

    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters: ', end='')
    for letter in missedLetters:
        print(letter, end='')
    print()

    blanks = '_'*len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')

    print()



showBlank('', 'ti', 'tictactoe')
    # if letter in secretWord and not stateWord.isalpha():
    #     splittedWord = secretWord.split(letter)

    #     for item in range(len(splittedWord)):
    #         splittedWord[item] = '_'*len(splittedWord[item])       
    #     stateWord = letter.join(splittedWord)

    # elif letter in secretWord and stateWord.isalpha():
    #     splittedWord = secretWord.split(letter)


    # return stateWord
    




# playAgain = 'yes'
# playerLife = 6
# letter = ','
# guessWord = getSecretWord()
# currentStateWord = '_'*len(guessWord) 


# while playAgain == 'yes' or playAgain == 'Yes':

#     showDrawing(playerLife)
#     print("- Secret Word: " + showBlank(guessWord, letter))

#     print('\n\nGuess a letter: ')
#     letter = input()

#     if letter not in guessWord:
#         playerLife -= 1
    