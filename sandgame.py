import oop
import pygame
import math
import time

background_color = (0,0,0) 
  
# Define the dimensions of 
# screen object(width,height) 
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
GRID_SIZE = 50
NUM = 0
RATE = 30
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
  
# Set the caption of the screen 
pygame.display.set_caption('sand game') 
  
# Fill the background colour to the screen 
screen.fill(background_color) 
  
# Update the display using flip 
pygame.display.flip() 
  
# Variable to keep our game loop running 
running = True
# game loop
gameboard = [[0 for _ in range(math.floor(WINDOW_WIDTH/GRID_SIZE))] for _ in range(math.floor(WINDOW_HEIGHT/GRID_SIZE))]
TIME_BOARD = [[0 for _ in range(math.floor(WINDOW_WIDTH/GRID_SIZE))] for _ in range(math.floor(WINDOW_HEIGHT/GRID_SIZE))]
while running: 
    #screen.fill(background_color)
    sandgame = oop.sandgame(GRID_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT, screen, pygame.Color(100,203,5))
    MOUSE_POS = pygame.mouse.get_pos()
    ev = pygame.event.get()

    # proceed events
    for event in ev:

        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONDOWN:
            sandgame.createsand(MOUSE_POS)
            gameboard[(MOUSE_POS[1] // GRID_SIZE)][(MOUSE_POS[0] // GRID_SIZE)] = 1
    for i in range(math.floor(WINDOW_WIDTH/GRID_SIZE)):
        for j in range(math.floor(WINDOW_HEIGHT/GRID_SIZE)):
            if gameboard[i][j] == 1:
                TIME_BOARD[i][j]+=1
            elif gameboard[i][j] == 0 and TIME_BOARD[i][j] > 0:
                TIME_BOARD[i][j] = 0

    for i in range(math.floor(WINDOW_WIDTH/GRID_SIZE)):
        for j in range(math.floor(WINDOW_HEIGHT/GRID_SIZE)):
            if gameboard[i][j] == 1 and i != (math.floor(WINDOW_WIDTH/GRID_SIZE) - 1) and (TIME_BOARD[i][j]%RATE == 0) and (TIME_BOARD[i][j] > 0):
                if gameboard[i + 1][j] == 0:  # Only move sand if the cell below is empty
                    gameboard[i][j] = 0
                    gameboard[i + 1][j] = 1
                    sandgame.updatesandposition(((j * GRID_SIZE), (i + 1) * GRID_SIZE))
        
 #For loop through the event queue   
    for event in pygame.event.get(): 
      
        #Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
    pygame.display.update()
