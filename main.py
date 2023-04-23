import pygame
import sys
import random as r
import math
from pygame.locals import *
import time 

# Define the window for the game
WIN = pygame.display.set_mode((500, 500))
pygame.init()
font = pygame.font.SysFont("TimesNewRoman", 25, 1)

#display title in window
pygame.display.set_caption("50-50 Games")

"""
                ^     
                |
                |
 Window Setup and Package Imports
      
Upload images and sounds
        |
        |
        v
"""
title_screen = pygame.image.load("tileScreen1.png")
title_screen = pygame.transform.scale(title_screen, (500, 500))
htptile_screen = pygame.image.load("HTPtile.png")
htptile_screen = pygame.transform.scale(htptile_screen, (500, 500))
end_Screen = pygame.image.load("endScreen.png")
end_Screen = pygame.transform.scale(end_Screen, (500, 500))

jump_sound = pygame.mixer.Sound("jumpSound.wav")
backgroundMusic = pygame.mixer.Sound("backgroundMusic.wav")
unalivedSound = pygame.mixer.Sound("unalivedSound.wav")
wrongClick = pygame.mixer.Sound("wrongClick.wav")
backgroundMusic.set_volume(0.5)
backgroundMusic.play(-1)

"""
                ^
                |
                |
    
    Window Setup and Package Imports
    
    
    Colors
    
        | 
        | 
        v
"""

# Define the colors 
colors = {
    #"black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (180, 50, 0),
    "orange": (200, 128, 0),
    "yellow": (255, 255, 0),
    "green": (0, 255, 0),
    "green1": (0, 190, 0),
    "blue": (47, 54, 153),
    "purple": (255, 51, 255),
    "pink": (0, 0, 0),
    "gray": (160, 160, 160),
    "brown": (150, 75, 0),
    "black": (30, 30, 30),
    "gold": (255, 215, 0)


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



start_time = 0
end_time = 0

def calculate_elapsed_time():
    global start_time, end_time
    elapsed_time = 0
    if end_time > 0:
        elapsed_time = end_time - start_time
    return elapsed_time


    


# Define the player  
class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 20
        self.vel = 50
        self.eyes_open = True  
        self.last_blink_time = 0
        self.hitbox = (self.x, self.y, 30, 30)


    def draw(self):
        pygame.draw.circle(WIN, colors["black"], (self.x, self.y), self.height)
        pygame.draw.rect(WIN, colors["white"], (self.x-12, self.y-10, 8, 8))
        pygame.draw.rect(WIN, colors["white"], (self.x+5, self.y-10, 8, 8))
        pygame.draw.ellipse(WIN, colors["white"], (self.x-10, self.y+5, 20, 2))
        pygame.draw.circle(WIN, colors["black"], (self.x-7.25, self.y-6), 3)
        pygame.draw.circle(WIN, colors["black"], (self.x+9, self.y-6), 3)
        pygame.draw.rect(WIN, colors["orange"], (self.x+5, self.y+5, 12, 3))
        pygame.draw.rect(WIN, colors["white"], (self.x+10, self.y+5, 8, 3))
        pygame.draw.circle(WIN, colors["red"], (self.x+17, self.y+6.9), 2)

        

        # draw cowboy hat
        pygame.draw.ellipse(WIN, colors["brown"], (self.x-20, self.y-18, 40, 5))
        pygame.draw.rect(WIN, colors["brown"], (self.x-12.5, self.y-26, 26, 10))
        pygame.draw.rect(WIN, colors["black"], (self.x-12.5, self.y-20, 26, 4))
        pygame.draw.rect(WIN, colors["gold"], (self.x-5, self.y-20, 10, 4), 2, 2)

        
        line_thickness = 1
        line_length = 12
        num_lines = 3
        line_spacing = 4

        for i in range(num_lines):
            start_point = (self.x+17, self.y+6.9)
            end_point = (self.x+17, self.y+6.9-(line_length+i*line_spacing))
            pygame.draw.line(WIN, colors["gray"], start_point, end_point, line_thickness)
       
        current_time = time.time()
        if self.eyes_open:
            if current_time - self.last_blink_time > 4:
                self.eyes_open = False
                self.last_blink_time = current_time
        else:
            if current_time - self.last_blink_time > 0.5:
                self.eyes_open = True
                self.last_blink_time = current_time

        # draw the eyes 
        eye_color = colors["white"] if self.eyes_open else colors["black"]
        pygame.draw.rect(WIN, eye_color, (self.x-12, self.y-10, 8, 8))
        pygame.draw.rect(WIN, eye_color, (self.x+5, self.y-10, 8, 8))
        pygame.draw.circle(WIN, colors["black"], (self.x-7.25, self.y-6), 3)
        pygame.draw.circle(WIN, colors["black"], (self.x+9, self.y-6), 3)

    
    def movement(self):
        global jump_sound
        jump_sound.set_volume(0.5)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x > 0:
            time.sleep(0.2)
            self.x -= self.vel
            jump_sound.play()
            
        if keys[pygame.K_d] and self.x < 500 - self.width:
            time.sleep(0.2)
            self.x += self.vel
            jump_sound.play()
        
        if keys[pygame.K_w] and self.y > 0:
            time.sleep(0.2)
            self.y -= self.vel
            jump_sound.play()
            
        if keys[pygame.K_s] and self.y < 500 - self.height:
            time.sleep(0.2)
            self.y += self.vel
            jump_sound.play()

            

            


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
    pygame.draw.rect(WIN, colors["gray"], (0, 450, 500, 50))
    pygame.draw.rect(WIN, colors["gray"], (0, 0, 500, 50))
    pygame.draw.rect(WIN, colors["gray"], (0, 0, 0, 500))
    pygame.draw.rect(WIN, colors["gray"], (495, 0, 0, 500))
    
    lineY = 0
    lineX = 0

    # Draw the Y lines on the board

    for i in range(1, 10, 1):

        lineY = lineY + 50

        pygame.draw.rect(WIN, colors["gray"], (lineY, 50, 2, 400))

    # Draw the X lines on the board

    for i in range(1, 10, 1):

        lineX = lineX + 50

        pygame.draw.rect(WIN, colors["gray"], (0, lineX, 500, 2))

"""
               ^
               |
               |
       Background
       
       Paths 
        
        |
        |
        v
       
       
 """

path1 = [(175, 425), (175, 375), (175, 325), (175, 275), (175, 225), (175, 175), (175, 125), (175, 75)]


path2 = [(25, 125), (75, 125), (125, 125), (175, 125), (225, 125), (275, 125), (325, 125), (375, 125), (425, 125), (475, 125)]


path3 = [(25, 225), (75, 225), (125, 225), (175, 225), (175, 275), (175, 325), (175, 375), (175, 425)]


path4 = [(475, 125), (425, 125), (375, 125), (325, 125), (275, 125), (225, 125), (225, 175), (225, 225),(275, 225), (325, 225), 
         (375, 225), (425, 225), (475, 225)]

path5 = [(25, 225), (75, 225), (125, 225), (175, 225), (225, 225), (225, 275), (225, 325), (275, 325), (275, 375), (275, 425)]

path6 = [(175, 425), (175, 375), (225, 375), (275, 375), (325, 375), (325, 325), (375, 325), (425, 325), (425, 275), (425, 225), (475, 225)]


path7 = [(225, 75), (225, 125), (275, 125), (275, 175), (275, 225), (225, 225), (225, 275), (225, 325), (275, 325), (275, 375), (275, 425)]


path8 = [(125, 425), (125, 375), (125, 325), (125, 275), (175, 275), (175, 225), (175, 175), (225, 175), (225, 125), (275, 125),
         (325, 125), (325, 75)]

path9 = [(75, 425), (75, 375), (125, 375), (125, 325), (125, 275),
         (125, 225), (125, 175), (125, 125), (175, 125), (225, 125),
         (225, 175), (225, 225), (225, 275), (225, 325), (225, 375),
         (275, 375), (325, 375), (325, 325), (325, 275), (325, 225),
         (325, 175), (325, 125), (375, 125), (425, 125), (425, 175),
         (425, 225), (425, 275), (425, 325), (425, 375), (475, 375)]

path10 = [(25, 375), (75, 375), (125, 375), (125, 325), (125, 275), (175, 275), (225, 275), (225, 225),
          (225, 175), (275, 175), (325, 175), (325, 125), (325, 75)]

path11 = [(25, 425), (75, 425), (125, 425), (125, 375), (125, 325),
         (175, 325), (175, 275), (175, 225), (225, 225), (275, 225),
         (325, 225), (375, 225), (375, 175), (375, 125), (425, 125),
         (475, 125), (475, 75)]

path12 = [(25, 75), (25, 125), (75, 125), (125, 125), (175, 125),
         (175, 175), (175, 225), (225, 225), (275, 225), (325, 225),
         (325, 275), (325, 325), (375, 325), (425, 325), (425, 375),
         (475, 375)]

path13 = [(25, 425), (25, 375), (25, 325), (75, 325), (75, 275),
         (125, 275), (125, 225), (175, 225), (225, 225), (275, 225),
         (325, 225), (325, 275), (325, 325), (375, 325), (425, 325),
         (425, 275), (425, 225), (425, 175), (425, 125), (425, 75)]

path14 = [(25, 425), (75, 425), (75, 375), (75, 325), (125 ,325), (175, 325), (225, 325), (225, 275),
          (225, 225), (175, 225), (125, 225), (125, 175), (125, 125), (175, 125), (225, 125),
          (275, 125), (325, 125), (325, 75)]

path15 = [(125, 75), (125, 125), (75, 125), (75, 175), (75, 225), (75, 275), (75, 325), (75, 375), (125, 375),
          (175, 375), (175, 325), (175, 275), (225, 275), (225, 225), (225, 175), (275, 175), (275, 125), 
          (275, 75)]

path16 = [(375, 425), (375, 375), (425, 375), (425, 325), (425, 275),
         (425, 225), (425, 175), (425, 125), (375, 125), (325, 125),
         (325, 175), (325, 225), (275, 225), (275, 275), (275, 325),
         (225, 325), (225, 375), (225, 425)]

path17 = [(475, 75), (425, 75), (375, 75), (375, 125), (325, 125), 
         (325, 175), (325, 225), (375, 225), (425, 225),(425, 275),
         (425, 325), (375, 325), (325, 325), (275, 325), (275, 375), 
         (225, 375), (175, 375), (175, 325), (175, 275), (175, 225), 
         (125, 225), (75, 225), (75, 275), (25, 275)]

path18 = [(475, 375), (475, 325), (425, 325), (375, 325), (375, 375), 
         (325, 375), (275, 375), (275, 325), (275, 275), (275, 225), 
         (325, 225), (325, 175), (325, 125), (275, 125), (225, 125), 
         (225, 75), (175, 75), (125, 75), (75,75), (75, 125), (75, 175), 
         (75, 225), (25, 225)]

path19 = [(75, 425), (75, 375),
          (125, 375), (175, 375), (225, 375), (225, 325), (225, 275), (275, 275),
          (25, 375), (25, 325), (25, 275), (75, 275), (75, 225), (125, 225),
          (175, 225), (175, 175), (225, 175), (275, 175), (325, 175), (325, 125), (325, 75)]

path20 = [(225, 75), (225, 125), (225, 175), (225, 225), (225, 275), (275, 275), (275, 325), (275, 375),
          (275, 425), (275, 175), (325, 175), (375, 175), (375, 225), (375, 275), (225, 375), (175, 375),
          (125, 375), (125, 325), (125, 275), (125, 225), (75, 325), (25, 325)]

path21 = [(25,125), (75,125), (75, 175), (75, 225), (125, 125), (175, 125), (175, 175), (175, 225),
          (225, 125), (275, 125), (275, 175), (275, 225), (325, 125), (375, 125), (425, 125), (475, 125),
          (375, 175), (375, 225), (425, 225), (425, 275), (475, 275), (475, 325), (475, 375), (425, 375),
          (375, 375), (375, 325), (325, 325), (275, 325), (275, 375), (225, 375), (225, 425), (175, 425),
          (125, 425), (125, 375), (75, 375), (25, 375)]
          
path22 = [(325, 75), (325, 125), (375, 125), (375, 175), (375, 225), (325, 225), (325, 275),
          (325, 325), (375, 325), (425, 325), (425, 375), (425, 425), (375, 425), (325, 425),
          (275, 425), (275, 375), (225, 375), (175, 375), (175, 325), (175, 275), (225, 275),
          (225, 225), (225, 175), (175, 175), (175, 125), (125, 125), (75, 125), (75, 175),
          (75, 225), (75, 275), (25, 275)]

path23 = [(25, 275), (75, 275), (125, 275), (125, 225), (125, 175), (75, 175), (25, 175),
         (25, 125), (25, 75), (75, 75), (125, 75), (175, 75), (175, 125), (225, 125), (225, 175), (275, 175),
         (325, 175), (325, 225), (325, 275), (275, 275), (275, 325), (225, 325), (225, 375),
         (225, 425), (275, 425), (325, 425), (375, 425), (375, 375), (425, 375), (425, 325),
         (425, 275), (475, 275)]

path24 = [(475, 175), (425, 175),
         (425, 125), (375, 125), (325, 125), (325, 175), (325, 225),
         (375, 225), (375, 275), (425, 275), (425, 325), (425, 375), (375, 375), (325, 375),
         (275, 375), (225, 375), (225, 325), (225, 275), (175, 275), (175, 225), (175, 175),
         (225, 175), (225, 125), (225, 75), (175, 75), (125, 75), (125, 125), (75, 125), (75, 175),
         (75, 225), (75, 275), (25, 275), (25, 325), (25, 375), (75, 375), (75, 425)]

path25 = [(75, 75), (25, 75), (25, 125), (25, 175), (75, 175), (125, 175), (125, 125), (175, 125), (175, 75),
          (225, 75), (275, 75), (275, 125), (325, 125), (375, 125), (375, 75), (425, 75), (475, 75), (475, 125), (475, 175),
          (425, 175), (425, 225), (425, 275), (425, 325), (475, 325), (475, 375), (475, 425), (425, 425), (375, 425),
          (375, 375), (325, 375), (325, 325), (325, 275), (275, 275), (275, 225), (225, 225), (175, 225),
          (175, 275), (175, 325), (225, 325), (225, 375), (225, 425), (175, 425), (125, 425), (125, 375),
          (75, 375), (25, 375), (25, 425)]

path26 = [(25,325), (75, 325), (75, 375), (125, 375), (175, 375), (225, 375), (225, 325), (275, 325), (325, 325), (75, 275), 
          (75, 225), (125, 225), (125, 175), (125, 125), (175, 125), (225, 125), (275, 125), (275, 175), (325, 175), 
          (375, 175), (375, 125), (425, 125), (475, 125), (475, 175), (475, 225), (425, 225), (425, 275),
          (425, 325), (475, 325), (475, 375), (475, 425)]

path27 = [(25, 75), (25, 125), (75, 125), (125, 125), (125, 175), (125, 225), (125, 75), (175, 75), (225, 75),
          (275, 75), (275, 125), (325, 125), (375, 125), (375, 175), (375, 225), (375, 275), (325, 275), 
          (275, 275), (225, 275), (225, 325), (225, 375), (425, 275), (475, 275), (475, 325), (475, 375), (425, 375),
          (425, 425)]

path28 = [(275, 425), (275, 375), (275, 325), (325, 325), (375, 325), (375, 275), (375, 225), (375, 175),
          (375, 125), (425, 125), (325, 225), (275, 225), (275, 175), (225, 175), (175, 175), (125, 175),
          (75, 175), (25, 175), (125, 125), (125, 75), (75, 75), (25, 75), (125, 225), (125, 275),
          (75, 275), (75, 325), (75, 375), (125, 375), (125, 425)]



path29 = [(75, 425), (75, 375), (75, 325), (125, 325), (175, 325),
        (225, 325), (225, 375), (225, 425), (225, 275), (225, 225), (175, 225),
        (125, 225), (75, 225), (275, 225), (325, 225), (375, 225), (425, 225),
        (475, 225), (475, 175), (475, 125), (425, 125), (375, 125), (325, 125),
        (275, 125), (225, 125), (175, 125), (125, 125), (75, 125), (75, 75)]

path30 = [(175, 425), (175, 375), (125, 375), (125, 325), (125, 275),
        (175, 275), (225, 275), (225, 225), (225, 175), (225, 125), (175, 175),
        (275, 175), (275, 275), (325, 275), (325, 325), (325, 375), (275, 375),
        (275, 425), (375, 375), (375, 425), (425, 425), (475, 425), (475, 375),
        (475, 325), (475, 275), (475, 225), (475, 175), (475, 125), (425, 125),
        (375, 125), (375, 175), (425, 275), (375, 75), (325, 75)]
         
         
previous_positions = []


"""
            ^
            |
            |
 Paths for the player to follow
 
    Level function
    
        |
        |
        v
   
"""

#@function Level checks if the player is on a tile in the path
def Level(path_coords):
    global play, previous_positions, level, lives, clicks, remaining_clicks
    initial_clicks = [11, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20, 20, 25, 25, 30, 30, 30, 35, 35, 35, 35, 35, 35, 40, 40, 40, 40, 40, 40, 40] 


    # Check if the player is on a tile in the path
    current_pos = (play.x, play.y)
    if current_pos in path_coords:
        if current_pos not in previous_positions:
            previous_positions.append(current_pos)
        pygame.draw.rect(WIN, colors["gray"], (play.x-25, play.y-25, 50, 50))
    else:
        lives -= 1  # decrease lives by 1
        unalivedSound.set_volume(0.1)
        unalivedSound.play()
        
        if lives <= 0 and level < 7:
            print("Game Over")
            level = 0.5
        if lives <= 0 and level >= 7:
            print("Game Over")
            level = 0
        play.x, play.y = path_coords[0]
        previous_positions = [path_coords[0]]

    for pos in previous_positions:
        if pos in path_coords:
            pygame.draw.rect(WIN, colors["gray"], (pos[0]-25, pos[1]-25, 50, 50))

    play.draw()
    play.movement()

    # Check for mouse click and remaining clicks
    if remaining_clicks > 0:
        if pygame.mouse.get_pressed()[0]:
            clicks += 1
            time.sleep(0.06)
            remaining_clicks -= 1  
            wrongClick.set_volume(0.1)
            wrongClick.play()
            
            for pos in path_coords:
                if abs(pos[0] - pygame.mouse.get_pos()[0]) <= 30 and abs(pos[1] - pygame.mouse.get_pos()[1]) <= 30:
                    pygame.draw.rect(WIN, colors["gray"], (pos[0]-25, pos[1]-25, 50, 50))
                    remaining_clicks = remaining_clicks + 1
                    wrongClick.stop()

                    break
    else:
        # No remaining clicks, keep playing the current level
        pass
    #If player reaches the end of the path, increase level by 1
    if current_pos == path_coords[-1]:
        lives += 1
        level += 1
        remaining_clicks = initial_clicks[level]
        
    

        
    

        previous_positions = []

    if current_pos == path_coords[-1]:
        previous_positions = []
        

"""
         ^
         |
         |
    Level function
    Start & End Screen
         |
         |
         v
"""

#@function for How to play screen
def how_To_Play():
    global level
    WIN.blit(htptile_screen, (0, 0))
    if pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[0] >=  23 and pygame.mouse.get_pos()[0] <= 57:
            if pygame.mouse.get_pos()[1] >= 30 and pygame.mouse.get_pos()[1] <= 66:
                level = 0


#@function for start screen
def start_screen():
    global level, sys
    WIN.blit(title_screen, (0, 0))
    #function for start button if user clicks on the general area
    if pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[0] >= 148 and pygame.mouse.get_pos()[0] <= 351:
            if pygame.mouse.get_pos()[1] >= 288 and pygame.mouse.get_pos()[1] <= 321:
                    level = 1
        if pygame.mouse.get_pos()[0] >= 148 and pygame.mouse.get_pos()[0] <= 351:
            if pygame.mouse.get_pos()[1] >= 338 and pygame.mouse.get_pos()[1] <= 371:
                    level = 0.5
        if pygame.mouse.get_pos()[0] >= 148 and pygame.mouse.get_pos()[0] <= 351:
            if pygame.mouse.get_pos()[1] >= 388 and pygame.mouse.get_pos()[1] <= 421:
            
                pygame.quit()
                sys.exit()
                    
#@function for end screen
def end_screen():
    global level, calculate_elapsed_time, start_time, end_time, elapsed_time
    WIN.blit(end_Screen, (0, 0))
    
    elapsed_time = calculate_elapsed_time()
    minutes = int(elapsed_time / 60000)
    seconds = int(elapsed_time / 1000)
    milliseconds = int(elapsed_time % 60)

    if seconds >= 60:
        seconds = int(elapsed_time / 1000) % 60
        
    
    time_text = font.render("{}:{}:{:02d}".format(minutes ,seconds, milliseconds), True, colors["black"])
    WIN.blit(time_text, (220, 290))
    if pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[0] >=  0 and pygame.mouse.get_pos()[0] <= 500:
            if pygame.mouse.get_pos()[1] >= 0 and pygame.mouse.get_pos()[1] <= 500:
                level = 0
                
    

 


"""
         ^
         |
         |
    Start & End Screen
    
    
    Main function
         |
         |
         v
"""

clicks = 0
white_tiles = []
lives = 6
level = 0
remaining_clicks = 11

# Create an instance of the player
play = player(25, 475)

#@function for main game
def main():
    global lives, level, clicks, remaining_clicks, start_time, end_time, elapsed_time
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
            
            if level == 1 and start_time == 0:
                start_time = pygame.time.get_ticks()
            elif level == 26 and end_time == 0:
                end_time = pygame.time.get_ticks()

            # Calculate the elapsed time
            elapsed_time = calculate_elapsed_time()

        background()
        
        if level == 0:
          start_screen()
        elif level == 0.5:
            how_To_Play()
        elif level == 1:
            lives = 5
            Level(path1)
        elif level == 2:
            Level(path2)
        elif level == 3:
            Level(path3)
        elif level == 4:
            Level(path4)
        elif level == 5:
            Level(path5)
        elif level == 6:
            Level(path6)
        elif level == 7:
            Level(path7)
        elif level == 8:
            Level(path8)
        elif level == 9:
            Level(path9)
        elif level == 10:
            Level (path10)
        elif level == 11:
            Level(path11)
        elif level == 12:
            Level(path12)
        elif level == 13:
            Level(path13)
        elif level == 14:
            Level(path14)
        elif level == 15:
            Level(path15)
        elif level == 16:
            Level(path16)
        elif level == 17:
            Level(path17)
        elif level == 18:
            Level(path18)
        elif level == 19:
            Level(path19)
        elif level == 20:
            Level(path20)
        elif level == 21:
            Level(path21)
        elif level == 22:
            Level(path22)
        elif level == 23:
            Level(path23)
        elif level == 24:
            Level(path24)
        elif level == 25:
            Level(path25)
        elif level == 26:
            Level(path26)
        elif level == 27:
            Level(path27)
        elif level == 28:
            Level(path28)
        elif level == 29:
            Level(path29)
        elif level == 30:
            Level(path30)
        elif level == 31:
            end_screen()
        
        


        
        if level > 0.5 and level < 31:
            # Draw text
            lives_text = font.render("Lives: " + str(lives), 1, (0,0,0))
            WIN.blit(lives_text, (10, 15))
            # Draw clicks remaining until next level
            clicks_text = font.render("Sight: " + str(remaining_clicks) + "%", 1, (0,0,0))
            WIN.blit(clicks_text, (500/2 - clicks_text.get_width()/2, 15))
            levels_text = font.render("Level: " + str(level), 1, (0,0,0))
            WIN.blit(levels_text, (390, 15))
            

        pygame.display.update()

if __name__ == "__main__":
    main()
