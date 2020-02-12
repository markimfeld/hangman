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
    # if letter != '' and letter in secretWord:
    #     pos = secretWord.find(letter)
    #     repeatedTimes = secretWord.count(letter)
    finalWord = ''

    # if letter != '' and letter in secretWord:
    #     pos = secretWord.find(letter)
    #     timesRepeated = secretWord.count(letter)
    timesRepeated = secretWord.count(letter)
    for l in timesRepeated:
        if 


        

    print(finalWord)


    #     drawing = "_"*pos
    #     drawing += letter
    #     drawing += "_"* (nLetter-pos-1)
    #     print(repeatedTimes)
    # else:
    #     print("_"*nLetter)

showBlank('tictac','t')