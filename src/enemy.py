import pygame
import random
import src.utils as utils

from pathlib import Path

# Variables
enemy_img = pygame.image.load(Path('assets/enemy.png'))
max_value_move_x = utils.max_value_move_x(enemy_img)
numer_0f_enemies = 8

x_axis = []
y_axis = []
x_axis_change = []
y_axis_change = []

#Initialize variables
for i in range(numer_0f_enemies):
   x_axis.append(random.randint(0, int(max_value_move_x)))
   y_axis.append(random.randint(0, 200))
   x_axis_change.append(0.3)
   y_axis_change.append(50)


#handler enemy
def handler(screen: pygame.Surface, x: float, i: int):
   global x_axis_change, y_axis

   #keep inside screen
   if x <= 0 : 
      x_axis_change[i] = 0.3
      y_axis[i] += y_axis_change[i]
   elif x >= max_value_move_x : 
      x_axis_change[i] = -0.3
      y_axis[i] += y_axis_change[i]

   screen.blit(enemy_img, (x, y_axis[i]))