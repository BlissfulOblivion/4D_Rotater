import sys, os, pygame
from map_generator import *
from movement_mechanics import *
from pygame.locals import *


pygame.init()

# Initializes screen, tiles, and sprites
H,W = 360,360
screen = pygame.display.set_mode((H,W))

char = pygame.image.load('sprite.png').convert()
tiles = [pygame.image.load(str(i) + "tile.png").convert() for i in range(9)]

## TILES KEY
# 0 - blank
# 1 - grass
# 2 - waterground
# 3 - water
# 4 - fireground
# 5 - lava
# 6 - cloud
# 7 - sky
# 8 - pit

switchespos = [(1,(5,7)),(2,(7,7)),(3,(9,7))]

def activateswitch(switch):
    if switch == 0:
        for i in range(3):
            for j in range(3,5):
                maps[0][i][j] = '1'
        for i in range(3):
            for j in range(3,5):
                maps[1][i][j] = '0'
    if switch == 1:
        for i in range(3):
            for j in range(5,9):
                maps[0][i][j] = '1'
        for i in range(3):
            for j in range(5,9):
                maps[1][i][j] = '0'
    if switch == 2:
        for i in range(3):
            for j in range(9,12):
                maps[0][i][j] = '1'
        for i in range(3):
            for j in range(9,12):
                maps[1][i][j] = '0'


puzzles = ['puzzle3.txt','puzzle4.txt','puzzle7.txt']
x = 0
maps = genmap(puzzles[x])
curmap = 0
char = sprite(30,char,30)

rotated = False
while True:
    boundaries = []
    if rotated == False:
        if char.gridpos[0] == 0:
            boundaries.append("L")
        else:
            if maps[curmap][char.gridpos[1]][char.gridpos[0]-1] == 8:
                boundaries.append("L")
        
        if char.gridpos[0] == 11:
            boundaries.append("R")
        else:
            if maps[curmap][char.gridpos[1]][char.gridpos[0]+1] == 8:
                boundaries.append("R")
        
        if char.gridpos[1] == 0:
            boundaries.append("U")
        else:
            if maps[curmap][char.gridpos[1]-1][char.gridpos[0]] == 8:
                boundaries.append("U")
                
        if char.gridpos[1] == 11:
            boundaries.append("D")
        else:
            if maps[curmap][char.gridpos[1]+1][char.gridpos[0]] == 8:
                boundaries.append("D")
                
    elif rotated == True:
        if char.gridpos[0] == 0:
            boundaries.append("OUT")
        else:
            if rotmaps[char.gridpos[1]][char.gridpos[0]-1] == 8:
                boundaries.append("OUT")
    
        if char.gridpos[0] == 11:
            boundaries.append("IN")
        else:
            if rotmaps[char.gridpos[1]][char.gridpos[0]+1] == 8:
                boundaries.append("IN")
        
        if char.gridpos[1] == 0:
            boundaries.append("U")
        else:
            if rotmaps[char.gridpos[1]-1][char.gridpos[0]] == 8:
                boundaries.append("U")
                
        if char.gridpos[1] == 11:
            boundaries.append("D")
        else:
            if rotmaps[char.gridpos[1]+1][char.gridpos[0]] == 8:
                boundaries.append("D")
        
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_r:
                if rotated == True:
                    rotated,curmap = rotate(rotated,char,curmap,maps)
                else:
                    rotated,rotmaps = rotate(rotated,char,curmap,maps)
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
            elif event.key == K_u:
                if x == 0:
                    maps = genmap(puzzles[1])
                    curmap = 0
                    char.gridpos = [0,1]
                    x = 1
                elif x == 1:
                    maps = genmap(puzzles[2])
                    char.gridpos = [3,6]
                    curmap = 0
                    x = 2
                elif x == 2:
                    maps = genmap(puzzles[0])
                    char.gridpos = [0,1]
                    curmap = 0
                    x = 0
        if (curmap,char.gridpos) in switchespos:
            activateswitch(switchespos.index((curmap,char.gridpos)))
            
    if rotated == False:
        for row in range(12):
            for col in range(12):
                screen.blit(tiles[maps[curmap][col][row]], (row*30,col*30))
    else:
        for row in range(12):
            for col in range(12):
                screen.blit(tiles[rotmaps[col][row]], (row*30,col*30))
    screen.blit(char.image, (char.gridpos[0]*30, char.gridpos[1]*30))
    pygame.display.update()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
