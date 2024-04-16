""""

Main driver file

I used pygame to make board and app settings 
"""

import pygame as p
from Chess import engine

WIDTH = HEIGHT = 512 #400 another option
DIMENSION = 8 #8X8
SQ=SIZE = HEIGHT // DIMENSION
MAX_FPS = 24 #for animations another option 16 
IMAGES = {}

'''

'''

def loadImages():
   pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
   for piece in pieces:
      IMAGES[pieces] = p.image.load("images/" + pieces + ".png")
