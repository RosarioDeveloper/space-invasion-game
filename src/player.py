import pygame
from pathlib import Path

img_player = pygame.image.load(Path('assets/foguete.png'))


x = (800 / 2) - (img_player.get_width() / 2)
y = 536

#handler player
def handler(screen: pygame.Surface, x: float):
   maxPlayerMoveScreen = (800 - img_player.get_width())

   #keep inside screen
   if x <= 0 : x = 0
   if x >= maxPlayerMoveScreen : x = maxPlayerMoveScreen

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
