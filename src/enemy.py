import pygame
import random
import src.utils as utils

from pathlib import Path
from src.config import config

# Variables
enemy_img = pygame.image.load(Path('assets/enemy.png'))
x = random.randint(0, 736)
y = random.randint(0, 200)
x_change = 0.3
y_change = 50


#handler player
def handler(screen: pygame.Surface, x: float):
   global x_change, y
   max_value_to_move =  utils.max_value_to_move_x(enemy_img)

   #keep inside screen
   if x <= 0 : 
      x_change = 0.3
      y += y_change
   elif x >= max_value_to_move : 
      x_change = -0.3
      y += y_change

   screen.blit(enemy_img, (x, y))