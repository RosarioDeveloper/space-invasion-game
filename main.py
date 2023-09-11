import pygame
import math
import random
import src.player as player
import src.enemy as enemy

import src.utils as utils

# initialize game
pygame.init()
pygame.display.set_caption("Space Invasion")
screen = pygame.display.set_mode((utils.screen_with, utils.screen_height))
background = pygame.image.load("./assets/background.jpg")

score = 0

#Detect Collosion
def there_is_collision(x1: float, y1: float, x2: float, y2: float) -> bool:
   distance = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y2 -y1), 2))
   return True if distance < 27 else False

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
         if not (player.visible_bullet):
            player.bullet_x_axis = player.x_axis
            player.shoot(screen, player.bullet_x_axis, player.bullet_y_axis)


   #Change player and enemy Location
   player.x_axis += player.x_axis_change

   #Bullet Moviment
   if(player.bullet_y_axis <= -64):
      player.bullet_y_axis = 500
      player.visible_bullet = False

   if player.visible_bullet:
      player.shoot(screen, player.bullet_x_axis, player.bullet_y_axis)
      player.bullet_y_axis -= player.bullet_y_axis_change

   #Change enemy location
   for en in range(enemy.numer_0f_enemies):
      enemy.x_axis[en] += enemy.x_axis_change[en]
      
      #Collision
      collesion = there_is_collision(
         enemy.x_axis[en], enemy.y_axis[en], player.bullet_x_axis, player.bullet_y_axis
      )

      if(collesion):
         #Restart bullet position
         player.bullet_y_axis = 500
         player.visible_bullet = False

         #Count Scores
         score += 1

         #Restart enemy position
         enemy.x_axis[en] = random.randint(0, int(enemy.max_value_move_x))
         enemy.y_axis[en] = random.randint(0, 200)
         print(score)

      enemy.handler(screen, enemy.x_axis[en], en)

   
   player.handler(screen, player.x_axis)
   pygame.display.update()
