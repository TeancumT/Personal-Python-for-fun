import numpy as np
import sympy as syp
import math

def main():
    pass

def printBoardGame1(board):
    for i in board:
        for j in i:
            if j == '':
                print(" _",end="")
            else:
                print(j, end="")
        print('')
            

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
if __name__ == "__main__":
    main()