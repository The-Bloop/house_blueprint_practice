import pygame
from pygame.locals import *

#This python script reads extracts information from a Vector PDF.
import readVPDF as rd

rd.openPDF("basic_house.pdf")
items = rd.getLines(True)

#Initializing Pygame
pygame.init()
screen = pygame.display.set_mode((1000,1000))
screen.fill((0,0,0))
gameOn = True

i = 0

while gameOn:
    for event in pygame.event.get():
        if(event.type == KEYDOWN):
            if(event.key == K_LEFT):
                if(i < len(items)):
                    if(items[i][0] == 'l'):
                        #Draws line if the item is of 'line' type.
                        pygame.draw.line(screen, (255,255,255), (items[i][1][0] + 50, items[i][1][1] + 50), (items[i][2][0] + 50, items[i][2][1] + 50))
                    else:
                        print(items[i])
                    i += 1
                elif(i == len(items)):
                    print("All Lines Printed")
                    i+=200
            elif(event.key == K_BACKSPACE):
                gameOn = False
    #Updates the pygame screen
    pygame.display.flip()