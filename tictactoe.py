import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def boardGuide():
    print('This is your numbers guide to choose!')
    print("1|2|3")
    print("-+-+-")
    print("4|5|6")
    print("-+-+-")
    print("7|8|9")

def drawBoard(board):
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[1] + "|" + board[2] + "|" + board[3])


def getPlayerShape():
    shape = ''
    while True:
        print("Do you want to be X or O?")
        shape = input().upper()
        if shape in 'XO':
            break
        else:
            print('Choose between X or O')
    return shape

def getRandomTurn():
    return random.randint(0, 1)

def computerMove():
    

def playerMove(playerShape):
    print('What is your next move? (1-9)')
    playerMove = int(input())
    board[playerMove] = playerShape


print("Welcome to Tic-Tac-Toe!")
print()
boardGuide()
print()

playerShape = getPlayerShape()
IAShape = ''
computerTurn = getRandomTurn()
gameIsOver = False


while True:

    if not computerTurn: # computer starts
        pass
    else: # player starts
        drawBoard(board)
        playerMove(playerShape)
        computerTurn = False