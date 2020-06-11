import tkinter
import numpy as np
import sys
import random

COLLUMNS_SIZE = 7
ROWS_SIZE = 6

def New_Board():
    return np.zeros((ROWS_SIZE,COLLUMNS_SIZE))

def Check_Column(Board,Col):
    if Board[0][Col]==0:
        return True
    else:
        return False

def If_Game_Over(Board,Check,Choose,Player):
    #poziomo
    for x in range(4):
        if Board[Check][x]==Player and Board[Check][x+1]==Player and Board[Check][x+2]==Player and Board[Check][x+3]==Player:
            return 1
    #pionowo
    for x in range(3):
        if Board[x][Choose]==Player and Board[x+1][Choose]==Player and Board[x+2][Choose]==Player and Board[x+3][Choose]==Player:
            return 1
    #skosnie 1
    for x in range(COLLUMNS_SIZE-3):
        for y in range(ROWS_SIZE-3):
            if Board[y][x]==Player and Board[y+1][x+1]==Player and Board[y+2][x+2]==Player and Board[y+3][x+3]==Player:
                return 1
    #skosnie2
    for x in range(COLLUMNS_SIZE-3):
        for y in range(3, ROWS_SIZE):
            if Board[y][x]==Player and Board[y-1][x+1]==Player and Board[y-2][x+2]==Player and Board[y-3][x+3]==Player:
                return 1
        

def main():
    
    #Generate new board
    Board=New_Board()
    print(Board)
    GameOver=0
    Turn=random.randint(0,1)
    
    while GameOver==0:
        if Turn == 0:
            print("Player 1 Turn")
            Choose=int(input("Choose a column you want to drop a coin: "))
            while Check_Column(Board,Choose)==False:
                print("No empty space in that column")
                Choose=int(input("Choose a column you want to drop a coin: "))
            for x in range(ROWS_SIZE):
                if Board[5-x][Choose]== 0:
                    Board[5-x][Choose]=1
                    Check=5-x
                    break
            print(Board)
            if If_Game_Over(Board,Check,Choose,1):
                print("Player 1 won the game!")
                GameOver=1
            
        else:
            print("Player 2 Turn")
            Choose=int(input("Choose a column you want to drop a coin: "))
            while Check_Column(Board,Choose)==False:
                print("No empty space in that column")
                Choose=int(input("Choose a column you want to drop a coin: "))
            for x in range(ROWS_SIZE):
                if Board[5-x][Choose]== 0:
                    Board[5-x][Choose]=2
                    Check=5-x
                    break
            print(Board)
            if If_Game_Over(Board,Check,Choose,2):
                print("Player 2 won the game!")
                GameOver=1
        
        #Switch Turns
        Turn=(Turn+1)%2

main()