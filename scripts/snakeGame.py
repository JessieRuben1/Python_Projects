# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:39:13 2020

@author: admin
"""

import pygame
import math 
import random
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 20
    w = 500
    def __init__(self, start, dirnx=1, dirny=0,color=(255,0,0)):
        pass
    
    def move(self, dirnx, dirny): 
        pass
    
    def draw(self, surface, eyes=False):
        pass
    
    
class snake(object):
    def __init__(self, color, pos):
        pass
    def move(self):
        pass
    def reset(self, pos):
        pass
    def addCube(self):
        pass
    def draw(self, surface):
        pass
    
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows #Gives us the distance between the lines
    
    x = 0 #Keeps track of the current x
    y = 0 #Keeps track of the current y
    
    for l in range(rows): #We will draw one vertical and one horizontal line each loop
        x = x + sizeBtwn
        y = y + sizeBtwn
        
        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y))
    

def redrawWindow(surface):
    surface.fill((0,0,0)) #Fills the screen with black
    drawGrid(surface) #will draw our grid lines
    pygame.display.update() #update  the screen
    

def randomSnack(rows, item):
    pass

def message_box(surface, content):
    pass

def main():
    global width, rows, s
    width = 500 #width of our screen
    height = 500 #height of the screen 
    rows = 20 #Amount of rows
    
    win = pygame.display.set_mode((width, height)) #Creates our display objcect
    
    s = snake((255,0,0), (10, 10)) #creates the snake object
    
    clock = pygame.time.Clock() #creating a clock object
    
    flag = True
    #STARTING MAIN LOOP
    while flag:
        pygame.time.delay(50) #This will delay the game so it does not run too quickly
        clock.tick(10) #insures our game runs at 10fps
        redrawWindow(win) #this will refresh our display
        
    


main()
    