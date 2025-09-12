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

buis2 = pygame.Surface((80,200))
buis2.fill("green")

buis3 = pygame.Surface((80,300))
buis3.fill("green")

buis4 = pygame.Surface ((80,30))
buis4.fill("green")

buis5 = pygame.Surface((80, 120))
buis5.fill("green")

buis6 = pygame.Surface((80 , 200))
buis6.fill("green")

kutvogel = pygame.Surface((30,30))
kutvogel.fill("yellow")

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(surface, (00, 0))
  screen.blit(buis1, (180,0))
  screen.blit(buis2, (180,270))
  screen.blit(buis3, (400,0))
  screen.blit(buis4, (400,370))
  screen.blit(buis5, (620,0))
  screen.blit(buis6, (620, 220))
  screen.blit(kutvogel, (100, 230))

  pygame.display.update()
  clock.tick(60)
