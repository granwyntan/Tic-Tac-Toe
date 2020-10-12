#Implementation of Two Player Tic-Tac-Toe game in Python.

''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

instructionBoard = {'7': '7' , '8': '8' , '9': '9' ,
 '4': '4' , '5': '5' , '6': '6' ,
 '1': '1' , '2': '2' , '3': '3' }

board_keys = []
boardtype = int

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoardType1 function
    so that we can easily print the board everytime by calling this function. '''

def printBoardType1(board):
    print(' '+board['7'] + ' | ' + board['8'] + ' | ' + board['9']+' ')
    print('---+---+---')
    print(' '+board['4'] + ' | ' + board['5'] + ' | ' + board['6']+' ')
    print('---+---+---')
    print(' '+board['1'] + ' | ' + board['2'] + ' | ' + board['3']+' ')
def printBoardType2(board):
    print(' '+board['1'] + ' | ' + board['2'] + ' | ' + board['3']+' ')
    print('---+---+---')
    print(' '+board['4'] + ' | ' + board['5'] + ' | ' + board['6']+' ')
    print('---+---+---')
    print(' '+board['7'] + ' | ' + board['8'] + ' | ' + board['9']+' ')

def printWinner(turn):
    global boardtype
    globals()['printBoardType'+str(boardtype)](theBoard)
    print("\nGame Over.\n")
    print(" !!! " +turn+ " WON !!! ")
    print()
    
def gameStart():
    global boardtype
    choice = input("Top-Down [Default: 1] or Bottom-Top [2]? ")
    print()
    if choice == str(1) or 'top-down' in choice.lower():
        boardtype = 1
    elif choice == str(2) or 'bottom-top' in choice.lower():
        boardtype = 2
    else:
        boardtype = 1
    print("For each turn, the player, X or O, is to choose a position between 1 and 9, and if it is filled, they are to choose a new location, if all locations are filled up, and no one has won, it is a DRAW. If counters are 3 in a row, forming a straight line, the respective player for the counters, X or O, will WIN the game")
    print()
    globals()['printBoardType'+str(boardtype)](instructionBoard)

# Now we'll write the main function which has all the gameplay functionality.
def game():
    global boardtype

    turn = 'X'
    count = 0
    
    for i in range(10):
        print()
        globals()['printBoardType'+str(boardtype)](theBoard)
        print()
        print()

        move = input("It's your turn, " +turn+". Which position would you like to move to? ")

        if move:
            if (type(move) != str):
                print('Invalid Input')
                continue
            elif move.isnumeric():
                if (int(move) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]):
                    print('Invalid Input')
                    continue
                elif theBoard[move] == ' ':
                    theBoard[move] = turn
                    count += 1
                else:
                    print("That place is already filled.\nWhich position would you like to move to? ")
                    continue
            else:
                print('Invalid Input')
            # Now we will check if player X or O has won,for every move after 5 moves. 
            if count >= 5:
                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                    printWinner(turn)
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                    printWinner(turn)
                    break
                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                    printWinner(turn)
                    break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                    printWinner(turn)
                    break
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                    printWinner(turn)
                    break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                    printWinner(turn)
                    break
                elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                    printWinner(turn)
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                    printWinner(turn)
                    break

            # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            if count == 9:
                print("\nGame Over.\n")                
                print("It's a Tie!!")

            # Now we have to change the player after every move.
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        else:
            print('Invalid Input')
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to Play Again [Y/N]?")
    if "y" in restart.lower():  
        for key in board_keys:
            theBoard[key] = " "
        gameStart()
        game()
    
if __name__ == "__main__":
    gameStart()
    game()
