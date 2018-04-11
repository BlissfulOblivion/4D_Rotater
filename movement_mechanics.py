import pygame
from pygame.locals import *

# Sprite
class sprite:
    def __init__(self, speed, image, height):
        self.speed = speed      # How many pixels it moves per keydown
        self.image = image      # Sprite image
        self.height = height    # Sprite height -- used to measure movement
        self.pos = image.get_rect().move(0, -height) # Sets initial position on screen
        self.gridpos = [0,1]    # Sets initial grid position
        self.x = self.pos[0]    # Sets grid x position to initial x-position
        self.y = self.pos[1]    # Sets grid y position to initial y-position
        self.z = 1              # Sets grid z position to 1 to center it on the cross-section of plane 1
            
    # Defines movement method
    def move(self,direction,boundaries):
        if direction not in boundaries:
            if direction == "L":
                #self.pos = self.pos.move(-self.speed, 0)
                self.gridpos[0] -= 1
            elif direction == "R":
                #self.pos = self.pos.move(self.speed, 0)
                self.gridpos[0] += 1
            elif direction == "D":
                #self.pos = self.pos.move(0, self.speed)
                self.gridpos[1] += 1
            elif direction == "U":
                #self.pos = self.pos.move(0, -self.speed)
                self.gridpos[1] -= 1
            elif direction == "IN":
                #self.pos = self.pos.move(self.speed, 0)
                self.gridpos[0] += 1
            elif direction == "OUT":
                #self.pos = self.pos.move(-self.speed, 0)
                self.gridpos[0] -= 1


# Rotation mechanic
def rotate(rotated,char,curmap,maps):
    pos = char.gridpos[0]
    if pos == 0 or pos == 11:
        return rotated,curmap
    # If not rotated, return corresponding cross sections of all maps
    if rotated == False:
        rotated = True
        rotatedmap = [[0 for col in range(12)] for row in range(12)]
        for mapp in range(len(maps)):
            for row in range(12):
                rotatedmap[row][mapp*3] = maps[mapp][row][pos-1]
                rotatedmap[row][1+mapp*3] = maps[mapp][row][pos]
                rotatedmap[row][2+mapp*3] = maps[mapp][row][pos+1]
        char.x = char.gridpos[0]
        if curmap == 0:
            char.z = 1
        elif curmap == 1:
            char.z = 4
        elif curmap == 2:
            char.z = 7
        elif curmap == 3:
            char.z = 10
        char.gridpos[0] = char.z
        return rotated,rotatedmap
    # If rotated, return the map the sprite is on
    elif rotated == True:
        rotated = False
        if pos in range(0,3):
            curmap = 0
        elif pos in range(3,6):
            curmap = 1
        elif pos in range(6,9):
            curmap = 2
        elif pos in range(9,12):
            curmap = 3
        if pos in [0,3,6,9]:
            char.x -= 1
        if pos in [2,5,8,11]:
            char.x += 1
        char.z = pos
        char.gridpos[0] = char.x
        return rotated,curmap
    
    
    
    
    
    
    
    
    
