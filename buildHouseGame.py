import pygame
from pygame.locals import *

#This python script reads extracts information from a Vector PDF.
import readVPDF as rd

def transformLines(pose, count):
    global items
    global screen
    global mousePose
    global difX, difY

    j = 0
    difX = pose[0] - mousePose[0]
    difY = pose[1] - mousePose[1]

    while(j < count and j < len(items)):
        pygame.draw.line(screen, (255,255,255), (items[j][1][0] + difX, items[j][1][1] + difY), (items[j][2][0] + difX, items[j][2][1] + difY))
        j += 1
    
    


rd.openPDF("basic_house.pdf")
items = rd.getLines(True)
xMin, yMin, xMax, yMax = rd.getBBox(True)

xCenter = xMax - xMin
yCenter = yMax - yMin

#Initializing Pygame
pygame.init()
screen = pygame.display.set_mode((1000,1000))
screen.fill((0,0,0))
gameOn = True
mousePose = [xCenter,yCenter]
difX = 500 - mousePose[0]
difY = 500 - mousePose[1]

i = 0

while gameOn:
    for event in pygame.event.get():
        if(event.type == KEYDOWN):
            if(event.key == K_LEFT):
                if(i < len(items)):
                    if(items[i][0] == 'l'):
                        #Draws line if the item is of 'line' type.
                        pygame.draw.line(screen, (255,255,255), (items[i][1][0] + difX, items[i][1][1] + difY), (items[i][2][0] + difX, items[i][2][1] + difY))
                    else:
                        print(items[i])
                    i += 1
                elif(i == len(items)):
                    print("All Lines Printed")
                    i+=200
            elif(event.key == K_BACKSPACE):
                gameOn = False
        # Move the printed house based on cursor position
        elif(event.type == MOUSEBUTTONDOWN):
            #print(pygame.mouse.get_pos())
            if(pygame.mouse.get_pos() != mousePose):
                screen.fill((0,0,0))
                transformLines(pygame.mouse.get_pos(), i)
    #Updates the pygame screen
    pygame.display.flip()