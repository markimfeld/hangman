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

words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt otter owl panda
parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
skunk sloth snake spider stork swan tiger toad trout turkey turtle
weasel whale wolf wombat zebra'''.split()

def getSecretWord():
    secretWord = random.choice(words)
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
    