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

#Gloabl variables for window size
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 10 #Size of Cells

assert WINDOWWIDTH % CELLSIZE == 0, """window width must be a multiple of 
cell size"""
assert WINDOWHEIGHT % CELLSIZE == 0, """window height must be a multiple of
cell size"""

CELLWIDTH = WINDOWWIDTH / CELLSIZE # number of cells wide
CELLHEIGHT = WINDOWHEIGHT / CELLSIZE # Number of cells high

# set up the colours
BLACK =    (0,  0,  0)
WHITE =    (255,255,255)
DARKGRAY = (40, 40, 40)

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


def main():
    
    pygame.init()
    global DISPLAYSURF
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 
    pygame.display.set_caption('Game Of Life') 
    
    DISPLAYSURF.fill(WHITE) #fills the screen white
    lifeDict = blankGrid() #Creating an empty board

    drawGrid() #draw the game grid
    pygame.display.update() #update the screen

    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        drawGrid() #draw the game grid
        pygame.display.update()


if __name__=='__main__':
    main()

