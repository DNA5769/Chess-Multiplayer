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
DARK_GREEN = (51, 102, 0)
BLUE = (0, 0, 255)
BLOCK_COLORS = (WHITE, DARK_GREEN)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Multiplayer")
clock = pygame.time.Clock()     ## For syncing the FPS

def draw(screen, g, selected):
  # Draws board
  for i in range(8):
    block_color_pointer = i%2
    for j in range(8):
      pygame.draw.rect(screen, BLOCK_COLORS[block_color_pointer], pygame.Rect(i*BLOCK, j*BLOCK, BLOCK, BLOCK))
      block_color_pointer = (block_color_pointer+1)%2

  # Draws Pieces
  for i in range(8):
    for j in range(8):
      piece = g.board[i][j]
      if piece is not None:
        picture = pygame.image.load(piece.img)
        picture = pygame.transform.scale(picture, (BLOCK, BLOCK))

        screen.blit(picture, (piece.pos[1]*BLOCK, piece.pos[0]*BLOCK))
  
  # Selection Box
  if selected is not None:
    pygame.draw.rect(screen, RED, pygame.Rect(selected[1]*BLOCK, selected[0]*BLOCK, BLOCK, BLOCK), 2)

## Game loop
running = True
g = Game()
color = 'W'
selected = None
while running:
    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

        # handle MOUSEBUTTONDOWN
        if event.type == pygame.MOUSEBUTTONDOWN:
          pos = pygame.mouse.get_pos()

          if selected is None:
            c, r = pos[0]//BLOCK, pos[1]//BLOCK
            selected = (r, c)
          else:
            selected = None

    #2 Draw/render
    screen.fill(BLACK)

    draw(screen, g, selected)

    pygame.display.update()       

pygame.quit()