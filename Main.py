import sys, os, pygame, puzzles
import numpy as np
from movement_mechanics import *
from pygame.locals import *


pygame.init()

# Initializes screen, tiles, and sprites
H,W = 360,360
screen = pygame.display.set_mode((H,W))

char = pygame.image.load('sprite.png').convert()
tiles = [pygame.image.load(str(i) + "tile.png").convert() for i in range(9)]


maps = puzzles.puzzle4
curmap = maps[0]
char = sprite(30,char,30)

rotated = False
while True:
    boundaries = []
    if char.gridpos[0] == 0:
        if rotated == False:
            boundaries.append("L")
        elif rotated == True:
            boundaries.append("OUT")
    else:
        if curmap[char.gridpos[0]-1][char.gridpos[1]] in [0,3,5,7,8]:
            if rotated == False:
                boundaries.append("L")
            elif rotated == True:
                boundaries.append("OUT")
    
    if char.gridpos[0] == 11:
        if rotated == False:
            boundaries.append("R")
        elif rotated == True:
            boundaries.append("IN")
    else:
        if curmap[char.gridpos[0]+1][char.gridpos[1]] in [0,3,5,7,8]:
            if rotated == False:
                boundaries.append("R")
            elif rotated == True:
                boundaries.append("IN")
    
    if char.gridpos[1] == 0:
        boundaries.append("U")
    else:
        if curmap[char.gridpos[0]][char.gridpos[1]-1] in [0,3,5,7,8]:
            boundaries.append("U")
            
    if char.gridpos[1] == 11:
        boundaries.append("D")
    else:
        if curmap[char.gridpos[0]][char.gridpos[1]+1] in [0,3,5,7,8]:
            boundaries.append("D")
        
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_r:
                rotated,curmap = rotate(rotated,char,curmap,maps)
            elif event.key == K_DOWN:
                char.move("D",boundaries)
            elif event.key == K_UP:
                char.move("U",boundaries)
            elif event.key == K_RIGHT:
                if rotated == True:
                    char.move("IN",boundaries)
                else:
                    char.move("R",boundaries)
            elif event.key == K_LEFT:
                if rotated == True:
                    char.move("OUT",boundaries)
                else:
                    char.move("L",boundaries)
            
    for row in range(0,12):
        for col in range(0,12):
            screen.blit(tiles[curmap[row][col]], (row*30,col*30))
    screen.blit(char.image, (char.gridpos[0]*30, char.gridpos[1]*30))
    pygame.display.update()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    