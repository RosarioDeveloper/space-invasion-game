import pygame

import src.player as player
import src.enemy as enemy

from src.config import config

# initialize game
pygame.init()

pygame.display.set_caption("Space Invasion")
screen = pygame.display.set_mode((config.screen_with, config.screen_height))

running = True
while running:
   screen.fill("purple")

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False

      if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
         player.x_change = player.move(event)

   #Change player location
   player.x += player.x_change
   player.handler(screen, player.x)

   #Enemies
   enemy.x += enemy.x_change
   enemy.handler(screen, enemy.x)

   pygame.display.update()
