import pygame
from pygame.locals import *

import readVPDF as rd

rd.openPDF("basic_house.pdf")
items = rd.getLines()


def drawLine(item):
    pygame.draw.line(screen, (255,255,255), (item[1][0], item[1][1]), (item[2][0], item[2][1]))

pygame.init()
screen = pygame.display.set_mode((1000,1000))
screen.fill((0,0,0))
i = 4

gameOn = True

while gameOn:
    while (i<len(items)):
        for event in pygame.event.get():
            if(event.type == KEYDOWN):
                if(event.key == K_LEFT):
                    if(items[i][0] == 'l'):
                        pygame.draw.line(screen, (255,255,255), (items[i][1][0] + 50, items[i][1][1] + 50), (items[i][2][0] + 50, items[i][2][1] + 50))
                    else:
                        print(items[i])
                    i += 1
                elif(event.key == K_BACKSPACE):
                    gameOn = False
        pygame.display.flip()
    if(i == len(items)):
        print("All Lines Drawn")
        i+=200

for item in items():
    if(item[0] == 'l'):
        pygame.draw.line(screen, (255,255,255), (item[1][0], item[1][1]), (item[2][0], item[2][1]))