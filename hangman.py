import random
import os

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
    '''
    +---+
   [O   |
   /|\  |
   / \  |
       ===
    ''',
    '''
    +---+
   [O]  |
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
weasel whale wolf wombat zebra kiko tito kanguro'''.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):

    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters: ', end='')
    for letter in missedLetters:
        print(letter, end='')
    print()

    blanks = '_'*len(secretWord)

    # replace the blanks for the correctLetters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')

    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the
    # player entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function return True if the player wants to play again, otherwise return False
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if the player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\n After ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guess, the word was "' + secretWord + '" ')
            gameIsDone = True
    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break


# def checkLetters(missedLetters, correctLetters, letters, secretWord):
#     if letters in secretWord and letters not in correctLetters:
#         correctLetters += letters
#     elif letters not in secretWord and letters not in missedLetters:
#         missedLetters += letters
#     else:
#         print("Ya ingresaste esa letra guanaco! Probá otra...")

#     return missedLetters, correctLetters

# def resetValues(missedLetters, correctLetters, secretWord):
#     missedLetters = ''
#     correctLetters = ''
#     secretWord = getRandomWord(WORDS)
#    return missedLetters, correctLetters, secretWord

# print('H A N G M A N')
# playAgain = 'yes'
# missedLetters = ''
# correctLetters = ''
# secretWord = getRandomWord(WORDS)

# while playAgain == 'yes' or playAgain == 'Yes':
#     displayBoard(missedLetters, correctLetters, secretWord)
#     print()
#     letters = input('Guess a letter: ')
#     missedLetters, correctLetters = checkLetters(missedLetters, correctLetters, letters, secretWord)
#     os.system('clear')
#     if missedLetters.__len__() > 6:
#         missedLetters, correctLetters, secretWord = resetValues(missedLetters, correctLetters, secretWord)
#         print("Perdiste!")
#         print("Play Again? yes or no", end=" ")
#         playAgain = input()
#         os.system('clear')
#     elif correctLetters.__len__() == secretWord.__len__():
#         missedLetters, correctLetters, secretWord = resetValues(missedLetters, correctLetters, secretWord)
#         print("Ganaste guanaco!")
#         print("Play Again? yes or no", end=" ")
#         playAgain = input() 
#         os.system('clear')
    


        
