
import pygame
import sys
import random as r
import math
from pygame.locals import *
import time 

# Define the window for Game to be played in
WIN = pygame.display.set_mode((500, 500))
pygame.init()

"""
    Colors
    
        | 
        | 
        v
"""

# Define the colors to be used in the game
colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "orange": (255, 128, 0),
    "yellow": (255, 255, 0),
    "green": (0, 255, 0),
    "green1": (0, 190, 0),
    "blue": (0, 0, 220),
    "purple": (255, 51, 255),
    "pink": (0, 0, 0),
}

"""       
        ^
        |
        |
     Colors
    Player Class
        |
        |
        v
"""
# Define the player  
class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 20
        self.vel = 50


    def draw(self):
        pygame.draw.circle(WIN, colors["black"], (self.x, self.y), self.height)


    
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x > 0:
            time.sleep(0.2)
            self.x -= self.vel
        if keys[pygame.K_d] and self.x < 500 - self.width:
            time.sleep(0.2)
            self.x += self.vel
        if keys[pygame.K_w] and self.y > 0:
            time.sleep(0.2)
            self.y -= self.vel
        if keys[pygame.K_s] and self.y < 500 - self.height:
            time.sleep(0.2)
            self.y += self.vel

"""
                ^
                |
                |
                
            Player Class 
            Background
       
                |
                |
                v
                              """



# Define the Background
def background():
    
    WIN.fill(colors["blue"])
    pygame.draw.rect(WIN, colors["white"], (0, 450, 500, 50))
    pygame.draw.rect(WIN, colors["white"], (0, 0, 500, 50))
    pygame.draw.rect(WIN, colors["white"], (0, 0, 0, 500))
    pygame.draw.rect(WIN, colors["white"], (495, 0, 0, 500))
    
    lineY = 0
    lineX = 0
    # Draw the Y lines on the board
    for i in range(1, 10, 1):
        lineY = lineY + 50
        pygame.draw.rect(WIN, colors["black"], (lineY, 50, 2, 400))
    # Draw the X lines on the board
    for i in range(1, 10, 1):
        lineX = lineX + 50
        pygame.draw.rect(WIN, colors["black"], (0, lineX, 500, 2))


"""
               ^
               |
               |
       Background
       
       Function For level 1
       
                |
                |
                v
                              """


# Define Level 1
previous_positions = []
def level1():
    global play, previous_positions, level, lives 
    
    # Define the coordinates of each tile in the path
    path_coords = [(25, 425), (75, 425), (125, 425),(125, 375), (125, 325),
     (175, 325), (175, 275), (175, 225), (225, 225), (275, 225), (325, 225), 
     (375, 225), (375, 175), (375, 125), (425, 125), (475, 125), (475, 75)]
    # Check if the player is on a tile in the path
    current_pos = (play.x, play.y)
    if current_pos in path_coords:

        if current_pos not in previous_positions:
            previous_positions.append(current_pos)

        pygame.draw.rect(WIN, colors["white"], (play.x-25, play.y-25, 50, 50))

    else:
        play.x, play.y = path_coords[0]
        previous_positions = [path_coords[0]]
        
    for pos in previous_positions:
        if pos in path_coords:
            pygame.draw.rect(WIN, colors["white"], (pos[0]-25, pos[1]-25, 50, 50))

    

    

    play.draw()
    play.movement()

    if current_pos == path_coords[-1]:
        play.x, play.y = path_coords[0]
        level = 2
        previous_positions = []
"""
level 1


level 2

"""

def level2():
    global play, previous_positions, level, lives
    
    # Define the coordinates of each tile in the path
    path_coords = [(25, 425), (25, 375), (25, 325),
                   (75, 325), (75, 275), (125, 275), (125, 225),
                   (175, 225), (225, 225), (275, 225), (325, 225),
                   (325, 275), (325, 325), (375, 325), (425, 325),
                   (425, 275), (425, 225), (425, 175), (425, 125), (425, 75)]
    # Check if the player is on a tile in the path
    current_pos = (play.x, play.y)
    if current_pos in path_coords:

        if current_pos not in previous_positions:
            previous_positions.append(current_pos)

        pygame.draw.rect(WIN, colors["white"], (play.x-25, play.y-25, 50, 50))

    else:
        lives = lives - 1
        play.x, play.y = path_coords[0]
        previous_positions = [path_coords[0]]
        
    for pos in previous_positions:
        if pos in path_coords:
            pygame.draw.rect(WIN, colors["white"], (pos[0]-25, pos[1]-25, 50, 50))



    play.draw()
    play.movement()

    if current_pos == path_coords[-1]:
        level = 3
        previous_positions = []
"""
level 2

level 3 
"""
def level3():
    global play, previous_positions, level
    
    # Define the coordinates of each tile in the path
    path_coords = [(25, 75), (25, 125), (75, 125), (125, 125), (175, 125),(175, 175),
     (175, 225), (225, 225), (275, 225), (325, 225), (325, 275), 
     (325, 325), (375, 325), (425, 325), (425, 375), (475, 375)]
    # Check if the player is on a tile in the path
    current_pos = (play.x, play.y)
    if current_pos in path_coords:

        if current_pos not in previous_positions:
            previous_positions.append(current_pos)

        pygame.draw.rect(WIN, colors["white"], (play.x-25, play.y-25, 50, 50))

    else:
        play.x, play.y = path_coords[0]
        previous_positions = [path_coords[0]]
        
    for pos in previous_positions:
        if pos in path_coords:
            pygame.draw.rect(WIN, colors["white"], (pos[0]-25, pos[1]-25, 50, 50))



    play.draw()
    play.movement()

    if current_pos == path_coords[-1]:
        level = 4
        previous_positions = []


"""
level 3


level 4 
"""


def level4():
    global play, previous_positions, level
    
    # Define the coordinates of each tile in the path
    path_coords = [(125, 425), (125, 375), (125, 325),
                   (75, 325), (75, 275), (125, 275), (125, 225),
                   (175, 225), (225, 225), (275, 225), (325, 225),
                   (325, 275), (325, 325), (375, 325), (425, 325),
                   (425, 275), (425, 225), (425, 175), (425, 125), (425, 75)]
    # Check if the player is on a tile in the path
    current_pos = (play.x, play.y)
    if current_pos in path_coords:

        if current_pos not in previous_positions:
            previous_positions.append(current_pos)

        pygame.draw.rect(WIN, colors["white"], (play.x-25, play.y-25, 50, 50))

    else:
        play.x, play.y = path_coords[0]
        previous_positions = [path_coords[0]]
        
    for pos in previous_positions:
        if pos in path_coords:
            pygame.draw.rect(WIN, colors["white"], (pos[0]-25, pos[1]-25, 50, 50))



    play.draw()
    play.movement()

    if current_pos == path_coords[-1]:
        level = 5
        previous_positions = []


"""


level4







main function


"""
lives = 10
level = 1
# Create an instance of the player
play = player(25, 475)
# main function, where the game runs
def main():
    global lives, level
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False        
                pygame.quit()
                sys.exit()

            
        background()
        if level == 1:
            lives = 10
            level1()
        if level == 2:
            level2()
        if level == 3:
            level3()
        if level == 4:
            level4()
        elif lives == 0:
            level = 1


                  
        pygame.display.update()
        
        
main() 
