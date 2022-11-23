#Project 1- Tic_Tac_Toe Game
the_board = {'7':' ', '8':' ','9': ' ',
             '4':' ','5':' ','6':' ',
             '1':' ', '2':' ','3':' '}

board_keys = []

for key in the_board:
    board_keys.append(key)


def printBoard(board):
    """
    It prints the board
    
    :param board: a dictionary with keys '1-9'. Each key has a value of ' ' (a single space)
    """
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' +board['6']) 
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' +board['3']) 

def game():
    """
    The function game() is the main function of the game. It is the function that calls all the other
    functions.
    """
    turn = 'X'
    count = 0
    
    for i in range(10):
        printBoard(the_board)
        print("It is your turn, " + turn + ". Move to which place?")
        
        
        move = input()
        
        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print("That move is invalid, \nplease choose another move")
            continue
        
        #Now we will check if a player X or O  has won, for every move after 5 moves
        if count >=5:
            #check across the top
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ': 
                printBoard(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            #Check across middle
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':
                printBoard(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            #Check across bottom
            elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':
                printBoard(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            #Check down riht
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':
                printBoard(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            #Check down middle 
            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':
                printBoard(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            #Check down left
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':
                printBoard(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            #Check diagonal right
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':
                printBoard(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
             #Check diagonal left
            elif the_board['3'] == the_board['5'] == the_board['7'] != ' ':
                printBoard(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It is a tie.")
            
        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'
        
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do you want to restart the game?(y/n)")
        
    if restart == 'y' or restart =='Y':
        for key in board_keys:
            the_board[key] = " "
                
            
        game()
            
if __name__ == "__main__":
    game()
        
            
    




