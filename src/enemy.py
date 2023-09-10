import pygame
import random
import src.utils as utils

from pathlib import Path

# Variables
enemy_img = pygame.image.load(Path('assets/enemy.png'))
x_axis = random.randint(0, 736)
y_axis = random.randint(0, 200)
x_axis_change = 0.3
y_axis_change = 50


#handler enemy
def handler(screen: pygame.Surface, x_axis: float):
   global x_axis_change, y_axis
   x_axis_value =  utils.max_value_x_axis_move(enemy_img)

   #keep inside screen
   if x_axis <= 0 : 
      x_axis_change = 0.3
      y_axis += y_axis_change
   elif x_axis >= x_axis_value : 
      x_axis_change = -0.3
      y_axis += y_axis_change

   screen.blit(enemy_img, (x_axis, y_axis))