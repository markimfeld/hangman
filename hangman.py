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

PLAYER_LIFE = 0

def getSecretWord():
    secretWord = random.choice(WORDS)
    return secretWord

def showDrawing():
    if PLAYER_LIFE == 6:
        print(HANGMAN_PICS[0])
    elif PLAYER_LIFE == 5:
        print(HANGMAN_PICS[1])
    elif PLAYER_LIFE == 4:
        print(HANGMAN_PICS[2])
    elif PLAYER_LIFE == 3:
        print(HANGMAN_PICS[3])
    elif PLAYER_LIFE == 2:
        print(HANGMAN_PICS[4])
    elif PLAYER_LIFE == 1:
        print(HANGMAN_PICS[5])
    else:
        print(HANGMAN_PICS[6])


def showBlank(secretWord, letter):
    nLetter = secretWord.__len__()
    
    splittedWord = secretWord.split(letter)

    for item in range(len(splittedWord)):
        splittedWord[item] = '_'*len(splittedWord[item])       

    newSplittedWord = letter.join(splittedWord)

    print(newSplittedWord)

showBlank('tictac','a')