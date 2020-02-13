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

def showDrawing(playerLife):
    if playerLife == 6:
        print(HANGMAN_PICS[0])
    elif playerLife == 5:
        print(HANGMAN_PICS[1])
    elif playerLife == 4:
        print(HANGMAN_PICS[2])
    elif playerLife == 3:
        print(HANGMAN_PICS[3])
    elif playerLife == 2:
        print(HANGMAN_PICS[4])
    elif playerLife == 1:
        print(HANGMAN_PICS[5])
    else:
        print(HANGMAN_PICS[6])


def showBlank(secretWord, letter):
    
    newSplittedWord = '_'*len(secretWord)

    if letter in secretWord:
        splittedWord = secretWord.split(letter)

        for item in range(len(splittedWord)):
            splittedWord[item] = '_'*len(splittedWord[item])       

        newSplittedWord = letter.join(splittedWord)

    return newSplittedWord
    

playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'Yes':
    playerLife = 6
    guessWord = getSecretWord()
    showDrawing(playerLife)
    print("- Secret Word: " + showBlank(guessWord, letter=','))

    print('\n\nGuess a letter: ')
    letter = input()