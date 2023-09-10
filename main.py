import pygame

import src.player as player
import src.enemy as enemy

import src.utils as utils

# initialize game
pygame.init()

pygame.display.set_caption("Space Invasion")
screen = pygame.display.set_mode((utils.screen_with, utils.screen_height))
background = pygame.image.load("./assets/background.jpg")

running = True
while running:
   #Background
   screen.blit(background, (0,0))

   for event in pygame.event.get():

      #Closing Event
      if event.type == pygame.QUIT:
         running = False

      # Process key event
      if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
         player.x_axis_change = player.move(event)

      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
         player.shoot(screen, player.x_axis, player.bullet_y_axis)


   #Change player and enemy Location
   player.x_axis += player.x_axis_change
   enemy.x_axis += enemy.x_axis_change

   #Bullet Moviment
   if player.visible_bullet:
      player.shoot(screen, player.x_axis, player.bullet_y_axis)
      player.bullet_y_axis -= player.bullet_y_axis_change

   #Handler players and enemies
   player.handler(screen, player.x_axis)
   enemy.handler(screen, enemy.x_axis)

   pygame.display.update()
