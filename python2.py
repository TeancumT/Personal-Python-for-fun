import numpy as np
import sympy as syp
import math

def main():
    game1()
    game2()

def printBoardGame1(board):
    a=1
    print(' ', end="")
    for i in board[0]:
        print(' '+str(a), end = "")
        a+=1
    print('')
    a = 1
    for i in board:
        print(a,end = "")
        for j in i:
            if j == '':
                print(" _",end="")
            else:
                print(' '+j, end="")
        print('')
        a+=1

def editBoardGame1(height,length,board,xo):
    newBoard = eval(str(board))
    if height > 3 or height < 1 or length > 3 or length < 1:
        print("Error Not Able To Place")
    elif board[height-1][length-1] == '':
        newBoard[height-1][length-1] = str(xo)
    else:
        print("Can Not Place")
    return newBoard
    

def game1():
    board = eval("[['','',''],['','',''],['','','']]")
    truthy = True
    print("Want to play Tic Tac Toe?")
    print("Type 'no' or 'yes'")
    while truthy:
        a = input(' : ')
        if a == 'no':
            return None
        elif a == 'yes':
            truthy = False
        else:
            print('')
    printBoardGame1(board)
    print()
    board = editBoardGame1(3,1,board,"x")
    printBoardGame1(board)
    print()
    board = editBoardGame1(2,2,board,"o")
    printBoardGame1(board)
    print()
def game2():
    pass
if __name__ == "__main__":
    main()