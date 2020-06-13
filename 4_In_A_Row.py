import tkinter
import numpy as np
import sys
import random
import pygame
import math

COLLUMNS_SIZE = 7
ROWS_SIZE = 6

pygame.init()
Screen=pygame.display.set_mode((700,800))
pygame.display.set_caption('4_In_A_Row')
Font = pygame.font.SysFont("arial",50)
Font2 = pygame.font.SysFont("arial",25)
Font3 = pygame.font.SysFont("arial",80)
Font4 = pygame.font.SysFont("arial",15)
mainClock = pygame.time.Clock()

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
        
def If_Full(Board):
    Empty_Space=0
    for x in range(COLLUMNS_SIZE):
        for y in range(ROWS_SIZE):
            if Board[y][x]==0:
                Empty_Space+=1
    if Empty_Space == 0:
        return True
    else:
        return False
    
def Draw_Board(Board):
    for x in range(COLLUMNS_SIZE):
        for y in range(ROWS_SIZE):
            pygame.draw.rect(Screen,(0,255,0),(x*100,(y+2)*100,100,100))
            pygame.draw.circle(Screen,(0,0,0),(x*100+50,(y+2)*100+50,),40)

def Draw_Circles_After_Move(Board):
    for x in range(COLLUMNS_SIZE):
        for y in range(ROWS_SIZE):
            if Board[y][x]==1:
                pygame.draw.circle(Screen,(255,0,0),(x*100+50,(y+2)*100+50,),40)
            elif Board[y][x]==2:
                pygame.draw.circle(Screen,(255,255,0),(x*100+50,(y+2)*100+50,),40)

def Main_Menu():
    while True:
        Screen.fill((255,255,255))

        mx, my = pygame.mouse.get_pos()

        Start_Button = pygame.draw.rect(Screen,(0,255,0),(250,200,200,80))
        Quit_Button = pygame.draw.rect(Screen,(255,0,0),(250,400,200,80))
        Welcome= Font3.render("|Four In A Row|",1,(0,0,0))
        Screen.blit(Welcome,(85,10))
        Start= Font2.render("Start Game",1,(0,0,0))
        Screen.blit(Start,(285,150))
        Quit= Font2.render("Quit Game",1,(0,0,0))
        Screen.blit(Quit,(285,350))

        Press = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Press = True
                    if Start_Button.collidepoint((mx, my)):
                        if Press:
                            Game_Loop()
                    if Quit_Button.collidepoint((mx, my)):
                        if Press:
                            pygame.quit()
                            sys.exit()

        pygame.display.update()
        mainClock.tick(60)                    
def Game_Loop():
    
    #Generate new board
    Board=New_Board()
    print(Board)
    GameOver=0
    Turn=random.randint(0,1)
    Screen.fill((255,255,255))
    Draw_Board(Board)
    Button_0 = pygame.draw.rect(Screen,(80,80,80),(10,140,80,50))
    Button_1 = pygame.draw.rect(Screen,(80,80,80),(110,140,80,50))
    Button_2 = pygame.draw.rect(Screen,(80,80,80),(210,140,80,50))
    Button_3 = pygame.draw.rect(Screen,(80,80,80),(310,140,80,50))
    Button_4 = pygame.draw.rect(Screen,(80,80,80),(410,140,80,50))
    Button_5 = pygame.draw.rect(Screen,(80,80,80),(510,140,80,50))
    Button_6 = pygame.draw.rect(Screen,(80,80,80),(610,140,80,50))
    pygame.display.update()
    
    while GameOver==0:
        if Turn ==0:
            Which_Turn= Font.render("Player 1 Turn",1,(0,0,0))
            Screen.blit(Which_Turn,(200,10))
            pygame.display.update()
        else:
            Which_Turn= Font.render("Player 2 Turn",1,(0,0,0))
            Screen.blit(Which_Turn,(200,10))
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos() 
                print(event.pos)
                Go_On=False
                if Button_0.collidepoint((mx, my)):
                    if Check_Column(Board,0):
                        Choose=0
                        Go_On=True
                    else:
                        No_Space= Font2.render("Error : Choose another column",1,(0,0,0))
                        Screen.blit(No_Space,(180,100))
                        pygame.display.update()
                elif Button_1.collidepoint((mx, my)):
                    if Check_Column(Board,1):
                        Choose=1
                        Go_On=True
                    else:
                        No_Space= Font2.render("Error : Choose another column",1,(0,0,0))
                        Screen.blit(No_Space,(180,100))
                        pygame.display.update()
                elif Button_2.collidepoint((mx, my)):
                    if Check_Column(Board,2):
                        Choose=2
                        Go_On=True
                    else:
                        No_Space= Font2.render("Error : Choose another column",1,(0,0,0))
                        Screen.blit(No_Space,(180,100))
                        pygame.display.update()
                elif Button_3.collidepoint((mx, my)):
                    if Check_Column(Board,3):
                        Choose=3
                        Go_On=True
                    else:
                        No_Space= Font2.render("Error : Choose another column",1,(0,0,0))
                        Screen.blit(No_Space,(180,100))
                        pygame.display.update()
                elif Button_4.collidepoint((mx, my)):
                    if Check_Column(Board,4):
                        Choose=4
                        Go_On=True
                    else:
                        No_Space= Font2.render("Error : Choose another column",1,(0,0,0))
                        Screen.blit(No_Space,(180,100))
                        pygame.display.update()
                elif Button_5.collidepoint((mx, my)):
                    if Check_Column(Board,5):
                        Choose=5
                        Go_On=True
                    else:
                        No_Space= Font2.render("Error : Choose another column",1,(0,0,0))
                        Screen.blit(No_Space,(180,100))
                        pygame.display.update()
                elif Button_6.collidepoint((mx, my)):
                    if Check_Column(Board,6):
                        Choose=6
                        Go_On=True
                    else:
                        No_Space= Font2.render("Error : Choose another column",1,(0,0,0))
                        Screen.blit(No_Space,(180,100))
                        pygame.display.update()
                else:
                    Go_On=False
                if Go_On==True:
                    pygame.draw.rect(Screen,(255,255,255),(0,0,609,139))
                    if Turn == 0:
                        print("Player 1 Turn")                
                        for x in range(ROWS_SIZE):
                            if Board[5-x][Choose]== 0:
                                Board[5-x][Choose]=1
                                Check=5-x
                                break
                        print(Board)
                        Draw_Circles_After_Move(Board)
                        pygame.display.update()
                            
                        if If_Game_Over(Board,Check,Choose,1):
                            print("Player 1 won the game!")
                            pygame.draw.rect(Screen,(255,255,255),(0,0,609,139))
                            Gam_Ov= Font.render("!!!Player 1 Won!!!",1,(0,0,0))
                            Screen.blit(Gam_Ov,(160,10))
                            Returning= Font2.render("Returning to main menu...",1,(0,0,0))
                            Screen.blit(Returning,(220,100))
                            pygame.display.update()
                            GameOver=1
                            pygame.time.wait(3000)

                        if If_Full(Board):
                            print("Its a draw!")
                            pygame.draw.rect(Screen,(255,255,255),(0,0,609,139))
                            Gam_Ov= Font.render("!!!It's a draw!!!",1,(0,0,0))
                            Screen.blit(Gam_Ov,(180,10))
                            Returning= Font2.render("Returning to main menu...",1,(0,0,0))
                            Screen.blit(Returning,(220,100))
                            pygame.display.update()
                            GameOver=1
                            pygame.time.wait(3000)

                        
                    elif Turn == 1:
                        print("Player 2 Turn")                   
                        for x in range(ROWS_SIZE):
                            if Board[5-x][Choose]== 0:
                                Board[5-x][Choose]=2
                                Check=5-x
                                break
                        print(Board)
                        Draw_Circles_After_Move(Board)
                        pygame.display.update()
                            
                        if If_Game_Over(Board,Check,Choose,2):
                            print("Player 2 won the game!")
                            pygame.draw.rect(Screen,(255,255,255),(0,0,609,139))
                            Gam_Ov= Font.render("!!!Player 2 Won!!!",1,(0,0,0))
                            Screen.blit(Gam_Ov,(160,10))
                            Returning= Font2.render("Returning to main menu...",1,(0,0,0))
                            Screen.blit(Returning,(220,100))
                            pygame.display.update()
                            GameOver=1
                            pygame.time.wait(3000)

                        if If_Full(Board):
                            print("Its a draw!")
                            pygame.draw.rect(Screen,(255,255,255),(0,0,609,139))
                            Gam_Ov= Font.render("!!!It's a draw!!!",1,(0,0,0))
                            Screen.blit(Gam_Ov,(180,10))
                            Returning= Font2.render("Returning to main menu...",1,(0,0,0))
                            Screen.blit(Returning,(220,100))
                            pygame.display.update()
                            GameOver=1
                            pygame.time.wait(3000)
 
                    
                    #Switch Turns
                    Turn=(Turn+1)%2
                        
    mainClock.tick(60)
    
def main():
    Main_Menu()

main()