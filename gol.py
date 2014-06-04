#!/usr/bin/env python
# -*- coding: utf8 -*-
#==============================================================================
# FILE NAME: gol.py
# AUTHOR: Daniel Abril
# CREATED: Wed Jun  4 17:39:26 2014
# PROJECT: Game Of Life
#
#== DESCRIPTION: Python game of life:
#http://en.wikipedia.org/wiki/Conway's_Game_of_Life
#
#The Game of Life is in short a simulation of a group of cells. At every step
#in time, often referred to in the game as a tick, cells live or die depending
#on their surroundings.
#
#There are four rules which are applied simultaneously to all the cells in the
#game.
#
#1. Any live cell with fewer than two live neighbours dies, as if caused by
#under-population. 
#2. Any live cell with two or three live neighbours lives on to the next
#generation. 
#3. Any live cell with more than three live neighbours dies, as if by
#overcrowding. 
#4. Any dead cell with exactly three live neighbours becomes a live cell, as if
#by reproduction.
# 
# NOTES: Tutorial extracted from trevorappleton.blogspot.co.uk
# --> http://trevorappleton.blogspot.co.uk/2013/07/python-game-of-life.html 
#==============================================================================

import pygame, sys
from pygame.locals import *
import random

#Gloabl variables for window size
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 10 #Size of Cells

assert WINDOWWIDTH % CELLSIZE == 0, """window width must be a multiple of cell
size"""
assert WINDOWHEIGHT % CELLSIZE == 0, """window height must be a multiple of
cell size"""

CELLWIDTH = WINDOWWIDTH / CELLSIZE # number of cells wide
CELLHEIGHT = WINDOWHEIGHT / CELLSIZE # Number of cells high

# set up the colours
BLACK =    (0,  0,  0)
WHITE =    (240, 240, 240)
DARKGRAY = (40, 40, 40)
GREEN = (0, 255, 0)

#Updating time
#FPS = 61
MSEC = 200

def drawGrid():
    """ Draw a Grid """
    for x in range(0, WINDOWWIDTH, CELLSIZE): #drawing vertical lines
        #                             color     init    end
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x,0), (x, WINDOWHEIGHT))

    for y in range(0, WINDOWHEIGHT, CELLSIZE): #drawing horizontal lines
        #                             color     init    end
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0,y), (WINDOWWIDTH, y))

def blankGrid():
    """Create an empty dictionary representing an empty board (no cells):
    -> Board representation:
        #1 - cell alive
        #0 - cell died
    """
    gridDict = {}
    for y in range(CELLHEIGHT):
        for x in range(CELLWIDTH):
            gridDict[x,y]=0
    return gridDict

def startingGridRandom(lifeDict):
    """ Assign 0 or 1 to our cells by modifying the board grid dictionary"""
    
    for item in lifeDict:
        lifeDict[item] = random.randint(0, 1) #assign randomly 0 or 1
    return lifeDict

def startingRPentomino(lifeDict):
    """ Other starting potini:  R-pentomino 
    """
    x = CELLWIDTH / 2
    y = CELLHEIGHT / 2

    #R-pentomino
    lifeDict[x, y - 1] = 1
    lifeDict[x + 1, y - 1] = 1
    lifeDict[x - 1, y] = 1
    lifeDict[x, y] = 1
    lifeDict[x, y + 1] = 1
    return lifeDict

def startingAcorn(lifeDict):
    """ Other starting potini:  Acorn 
    """
    x = CELLWIDTH / 2
    y = CELLHEIGHT / 2

    #Acorn
    lifeDict[x - 3, y + 1] = 1
    lifeDict[x - 2, y + 1] = 1
    lifeDict[x + 1, y + 1] = 1
    lifeDict[x + 2, y + 1] = 1
    lifeDict[x + 3, y + 1] = 1
    lifeDict[x - 2, y - 1] = 1
    lifeDict[x, y] = 1
    return lifeDict

def colourGrid(item, lifeDict):
    """ Colorize alive cells """
    x = item[0]
    y = item[1]

    x = x * CELLSIZE # translates array into grid size
    y = y * CELLSIZE # translates array into grid size
    
    if lifeDict[item] == 0: #died cells
        #draw a white rectangle
        pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, CELLSIZE, CELLSIZE))

    if lifeDict[item] == 1: #alive cells
        #draw a green rectangle
        pygame.draw.rect(DISPLAYSURF, GREEN, (x, y, CELLSIZE, CELLSIZE))

    return None


def getNeighbours(item, lifeDict):
    """ Geti how many the neighbours has a cell """
    neighbours = 0

    for x in range(-1, 2):
        for y in range(-1, 2):
            checkCell = (item[0] + x, item[1] + y)
            if (checkCell[0] < CELLWIDTH and checkCell[0] >= 0 and checkCell[1]
                    < CELLHEIGHT and checkCell[1] >= 0):
                if lifeDict[checkCell] == 1:
                    if x == 0 and y == 0: 
                        neighbours += 0
                    else:
                        neighbours += 1
    return neighbours

def tick(lifeDict):
    """ Generation evolution """
    newTick = {}

    for item in lifeDict:
        numNeighbours = getNeighbours(item, lifeDict) #get number of neighbours
        if lifeDict[item] == 1: #alive cells
            if numNeighbours < 2 or numNeighbours > 3:
                #surrounding population < 2  or surrounding population > 3
                newTick[item] = 0 #cell dies
            else: #surrounding population = {2,3}
                newTick[item] = 1 #cell is still alive 
        elif lifeDict[item] == 0: #died cell
            if numNeighbours == 3: #reproduction
                newTick[item] = 1 #new cell created/resurrected 
            else:
                newTick[item] = 0 #cell still dead

    return newTick


def main():
    
    pygame.init()
    global DISPLAYSURF
    #FPSCLOCK = pygame.time.Clock() #controls time
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 
    pygame.display.set_caption('Game Of Life') 
    
    DISPLAYSURF.fill(WHITE) #fills the screen white
    lifeDict = blankGrid() #Creating an empty board
    #lifeDict = startingGridRandom(lifeDict) #Assign random life
    #lifeDict = startingRPentomino(lifeDict) #Assign R-pentomino life
    lifeDict = startingAcorn(lifeDict) #Assign Acorn life
    
    for item in lifeDict:
        colourGrid(item, lifeDict) #colorize board alive cells

    drawGrid() #draw the game grid
    pygame.display.update() #update the screen

    while True: #main game loop
        for event in pygame.event.get():
            if (event.type == QUIT or (event.type==KEYDOWN and
                event.key==K_ESCAPE)):
                pygame.quit()
                sys.exit()

        #retuns a tick/generation
        lifeDict = tick(lifeDict)

        #colouring the live cells, white the dead
        for item in lifeDict:
            colourGrid(item, lifeDict) #colorize board alive cells

        drawGrid() #draw the game grid
        pygame.display.update()
        #FPSCLOCK.tick(FPS)
        pygame.time.delay(MSEC)


if __name__=='__main__':
    main()

