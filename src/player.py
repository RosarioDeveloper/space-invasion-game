import pygame
import src.utils as utils

from src.config import config
from pathlib import Path


img_player = pygame.image.load(Path('assets/foguete.png'))

x = (config.screen_with / 2) - (img_player.get_width() / 2)
y = 500
x_change = 0

#handler player
def handler(screen: pygame.Surface, x: float):
   maxPlayerMoveScreenX = utils.max_value_to_move_x(img_player)

   #keep inside screen
   if x <= 0 : x = 0
   if x >=  maxPlayerMoveScreenX: x = maxPlayerMoveScreenX

   screen.blit(img_player, (x, y))

#handler player moviment
def move(event: pygame.event.Event) -> float:
   x_change = 0
   is_page_down = event.type == pygame.KEYDOWN

   # #Move plyer to left or Right
   if (is_page_down and event.key == pygame.K_LEFT):
      x_change = (- 0.3)

   if (is_page_down and event.key == pygame.K_RIGHT):
      x_change = 0.3

   return x_change
