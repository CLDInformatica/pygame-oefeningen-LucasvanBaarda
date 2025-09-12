'''
Gegeven zijn: een horror font dat "voetbal game" op het scherm zet en een plaatje van een bal.

We gaan de game aanpassen zodat het er beter uit ziet.

Doe het volgende:

  - Download een toepasselijk font en maak hiermee een scoreboard
  - Download 2 plaatjes van voetballers en zet deze tegenover elkaar op het scherm
  - Zet de bal in het midden van de scherm

Extra tijd:

  - Voeg 2 goals toe (links en rechts)
  - Voeg een toepasselijke achtergrond toe
  - Schrijf de namen van de spelers ergens op het scherm

Slides: https://docs.google.com/presentation/d/1c4C94q8OcMGCIFefVo18Xac4WIFJacq5Eutj1gY6rCg/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Voetbal game!')
clock = pygame.time.Clock()
running = True
Title_font = pygame.font.Font("Opdrachten/PyGame/Les2/fonts/212 Sports.otf", 50)

auto_surface = pygame.image.load("Opdrachten/PyGame/Les2/graphics/auto.png")
tekst_surface = Title_font.render("F1 Game", False, "white")

tekst1_surface = Title_font.render("Scoreboard", False, "white")

coureur1_surface = pygame.image.load("Opdrachten/PyGame/Les2/graphics/Hamilton.png")

coureur2_surface = pygame.image.load("Opdrachten/PyGame/Les2/graphics/Verstappen.png")

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  screen.blit(coureur1_surface, (0,0))
  screen.blit(coureur2_surface, (200,0))
  screen.blit(tekst_surface, (200, 100))
  screen.blit(auto_surface,  (90,50))
  screen.blit(tekst1_surface, (0,0))
  pygame.display.update()
  clock.tick(60)
