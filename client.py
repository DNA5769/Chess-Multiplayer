import pygame
import random
from Game import Game

WIDTH = HEIGHT = 400
BLOCK = WIDTH//8
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLOCK_COLORS = (WHITE, BLACK)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Multiplayer")
clock = pygame.time.Clock()     ## For syncing the FPS

def draw(screen):
  # Draws board
  for i in range(8):
    block_color_pointer = i%2
    for j in range(8):
      pygame.draw.rect(screen, BLOCK_COLORS[block_color_pointer], pygame.Rect(i*BLOCK, j*BLOCK, BLOCK, BLOCK))
      block_color_pointer = (block_color_pointer+1)%2 

## Game loop
running = True
while running:
    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

    #2 Draw/render
    screen.fill(BLACK)

    draw(screen)

    pygame.display.update()       

pygame.quit()