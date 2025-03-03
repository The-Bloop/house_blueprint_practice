#This is just a tutorial project. I got it from GeeksForGeeks Into to pygame tutorial.
#The link to this project is given below:
# https://www.geeksforgeeks.org/introduction-to-pygame/

import pygame

from pygame.locals import *

class Square(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Square,self).__init__()

        #Defining surface with dimensions X,Y
        self.surf = pygame.Surface((x,y)) 

        self.surf.fill((0,200,255))
        self.rect = self.surf.get_rect()

locations = [[40,40], [730,40], [730,530], [40,530]]

def moveSquares(dir):
    global locations
    loc = []
    #Clockwise
    if(dir == 1):
        loc.append(locations[3])
        loc.append(locations[0])
        loc.append(locations[1])
        loc.append(locations[2])
    #Counter Clockwise
    elif(dir == 2):
        loc.append(locations[1])
        loc.append(locations[2])
        loc.append(locations[3])
        loc.append(locations[0])

    locations = loc

    
pygame.init()

screen = pygame.display.set_mode((800,600))

squareTL = Square(20,20)
squareTR = Square(25,25)
squareBR = Square(30,30)
squareBL = Square(35,35)

gameOn = True

while gameOn:
    for event in pygame.event.get():
        print(event)
        #event.type is to define the type of Key action. KEYDOWN means event is triggered if a key is pushed down.
        #event.key is the exact key that is being pressed. 
        if (event.type == KEYDOWN):
            if(event.key == K_BACKSPACE):
                print('bs')
                gameOn = False
            elif(event.key == K_LEFT):
                print("Counter Clockwise")
                moveSquares(1)
            elif(event.key == K_RIGHT):
                print("Clockwise")
                moveSquares(2)

        elif (event.type == QUIT):
            print('Bye Bye')
            gameOn = False
        
    screen.fill((0,0,0))
    screen.blit(squareTL.surf, locations[0])
    screen.blit(squareTR.surf, locations[1])
    screen.blit(squareBR.surf, locations[2])
    screen.blit(squareBL.surf, locations[3])

    pygame.display.flip()