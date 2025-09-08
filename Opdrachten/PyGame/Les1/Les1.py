'''
Maak het plaatje dat in dit mapje staat na.

Slides: 
https://docs.google.com/presentation/d/1YwoUdeWABUYJkSfNzzZzDbCKvCVmWoo9Z5Uu7f_Y_K4/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Gamewindow set1')
clock = pygame.time.Clock()
running = True

surface = pygame.Surface((800, 400))
surface.fill("blue")

buis1 = pygame.Surface((80,200))
buis1.fill("green")


while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(surface, (00, 0))
  screen.blit(buis1, (180,0))
  
  pygame.display.update()
  clock.tick(60)
