import random
import math
from collections import Counter

################################################################################
def drawBoard(board,board_size):
    print ("  "+' '.join(str(x) for x in range(1,board_size+1)))
    for x in range(1,board_size+1):
        n=board_size*(board_size-x+1)
        print(" +"+'+'.join('-' for x in range(1,board_size+1))+"+")
        print(str(x)+"|"+'|'.join(board[n-y] for y in range(board_size-1,-1,-1))+"|")
    print(" +"+'+'.join('-' for x in range(1,board_size+1))+"+")
  

###############################################################################
def inputPlayerLetter():    #Lets player select letter
    letter=''
    while not (letter == 'X' or letter =='O'):
        print('Do you want to be X or O?')
        letter=input().upper()

    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

###############################################################################
def selectDifficulty():
    print("Please Select Difficulty Level")
    print("1-->Easy, 2-->Medium, 3-->Hard")
    return input()


###############################################################################
def whoGoesFirst(games):
    if games%2==0:
        return 'player'
    else:
        return 'computer'
   
############################################################################### 
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

###############################################################################
def makeMove(board,letter,move):
    if(board[move]==' '):
        board[move]=letter
    else:
        print ("Invalid move")
        print ("Play again with a Valid Move")
        return 0
    
#################################################################################
def isWinner(board, letter,board_size):
    for x in range(1,board_size+1):
        list1=[];
        for y in range(x,board_size*board_size+1,board_size):
            list1.append(board[y]);
        if(all(x==letter for x in list1)):
            return(1);
        
 
    for x in range(1,board_size*board_size+1,board_size): 
        list1=[];
        for y in range(x,x+board_size):
            list1.append(board[y]);
        if(all(x==letter for x in list1)):
            return(1);
      
    list1=[];
    for x in range(1,board_size*board_size+1,board_size+1):
        list1.append(board[x]);
    if(all(x==letter for x in list1)):
         return(1);
 
     
    list1=[];    
    for x in range(board_size,board_size*board_size,board_size-1):    
        list1.append(board[x]);
    if(all(x==letter for x in list1)):
        return(1);

################################################################################
def getBoardCopy(board):
    dupeBoard=[]

    for i in board:
        dupeBoard.append(i)
    return dupeBoard
    
################################################################################
def isBoardFull(board,board_size):
# Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, board_size*board_size+1):
        if isSpaceFree(board, i):
            return False
    return True
    
##############################################################################
def isSpaceFree (board,move):
    return board[move]==' '


##############################################################################
def getPlayerMove(board,board_size):
    string=' '.join(str(x) for x in range(1,board_size*board_size))
    move=' '
    while move not in string.split() or not isSpaceFree(board, int(move)):
        print("Next move")
        r,c=input().split(' ')
        r=int(r);
        c=int(c);
        return(board_size*(board_size-r+1)-(board_size-c))

################################################################################
def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

###############################################################################
def getComputerMove(board, computerLetter,difficulty,board_size):
    
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    if(difficulty == '1'):
        while True:
            move=random.choice(list(range(1,board_size*board_size+1)))
            if isSpaceFree(board, move):
                return move;
            
                 


    if(difficulty == '2'):
        for i in range(1, board_size*board_size+1):
            copy = getBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, computerLetter, i)
                if isWinner(copy, computerLetter,board_size):
                    return i
        for i in range(1, board_size*board_size+1):
            copy = getBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, playerLetter, i)
                if isWinner(copy, playerLetter,board_size):
                    return i

        while True:
            move=random.choice(list(range(1,board_size*board_size+1)))
            if isSpaceFree(board, move):
                return move;

    if(difficulty == '3'):
        for i in range(1, board_size*board_size+1):
            copy = getBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, computerLetter, i)
                if isWinner(copy, computerLetter,board_size):
                    return i
        for i in range(1, board_size*board_size+1):
            copy = getBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, playerLetter, i)
                if isWinner(copy, playerLetter,board_size):
                    return i
   
        list2=[]
        list4=[]
        for x in range(1,board_size+1):
            list1=[]
            list3=[]
            for y in range(x,board_size*board_size+1,board_size):
                list1.append(board[y])
                list3.append(y)
            list2.append(list1)
            list4.append(list3)
    
        for x in range(1,board_size*board_size+1,board_size): 
            list1=[]
            list3=[]
            for y in range(x,x+board_size):
                list1.append(board[y]);
                list3.append(y)
            list2.append(list1)
            list4.append(list3)
            
        list1=[]
        list3=[]
        for x in range(1,board_size*board_size+1,board_size+1):
            list1.append(board[x])
            list3.append(x)
        list2.append(list1)
        list4.append(list3)
    
        list1=[]
        list3=[]
        for x in range(board_size,board_size*board_size,board_size-1):    
            list1.append(board[x])
            list3.append(x)
        list2.append(list1)
        list4.append(list3)
        #print("ORIGINAL")
        #print (list2)
        #print (list4)
    
        idx=[]
        
        for l in range(0,len(list2)):
            for x in range(0,board_size):
                if (list2[l][x]==playerLetter):
                    idx.append(l)
                    break;
     
                    
        temp_list4 = []
        temp_list2=[]
        for i in range(0,len(list4)):
            if(i in idx):
                continue
            else:
                temp_list4.append(list4[i])
                temp_list2.append(list2[i])
        list4=temp_list4
        list2=temp_list2
       
            
        #print("AFTER REMOVING player moves")
        #print (list2)
        #print (list4)
        
        if len(list2)>0:
                list_counter=[]
                idx=[]
                for i in range(0,len(list4)):
                    c=Counter(list2[i])
                    #print(c)
                    list_counter.append([c['O'],i])
                
                #print(list_counter)
                temp=max(list_counter)
                #print(temp)
                temp_moves=[]
                for l in list_counter:
                    if l[0]==temp[0]:
                        temp_moves.append(l)
                #print(temp_moves)
                moves=[]
                for x in temp_moves:
                    for m in list4[x[1]]:
                        moves.append(m)
                if len(moves)>0:
                    while True:
                        move=random.choice(moves)
                        if isSpaceFree(board, move):
                            return move;
                else:
                     while True:
                         move=random.choice(list(range(1,board_size*board_size+1)))
                         if isSpaceFree(board, move):
                             return move;
               
        else:
              while True:
                 move=random.choice(list(range(1,board_size*board_size+1)))
                 if isSpaceFree(board, move):
                     return move;   
    


#################################################################################
##  MAIN FUNCTION
###############################################################################
print("Welcome to tic tac toe")
games=0
board_size=3
while True:
    theBoard = [' ']*(board_size*board_size+1)
    playerLetter,computerLetter = inputPlayerLetter()
    turn=whoGoesFirst(games)
    difficulty=selectDifficulty()
    if(difficulty == '1'):
        print("Difficulty Level: Easy")
    if(difficulty == '2'):
        print("Difficulty Level: Medium")
    if(difficulty == '3'):
        print("Difficulty Level: Hard")
    gameisplaying = True

    while gameisplaying:
        if turn == 'player':
            drawBoard(theBoard,board_size)
            move=getPlayerMove(theBoard,board_size)
            validMove=makeMove(theBoard,playerLetter,move)
        
            if isWinner(theBoard, playerLetter,board_size):
                drawBoard(theBoard,board_size)
                print('Player Wins!')
                gameIsPlaying = False
                break
            else:
                if isBoardFull(theBoard,board_size):
                    drawBoard(theBoard,board_size)
                    print('The game is a tie!')
                    break
                else:
                    if (validMove==0):
                        turn = 'player'
                    else:
                        turn = 'computer'

        else:
             # Computer’s turn.
             move = getComputerMove(theBoard, computerLetter,difficulty,board_size)
             makeMove(theBoard, computerLetter, move)
             if isWinner(theBoard, computerLetter,board_size):
                 drawBoard(theBoard,board_size)
                 print('Computer Wins!')
                 gameIsPlaying = False
                 break
             else:
                 if isBoardFull(theBoard,board_size):
                     drawBoard(theBoard,board_size)
                     print('The game is a tie!')
                     break
                 else:
                     turn = 'player'

    again=playAgain()
    if again:
        games+=1
    else:
        break
