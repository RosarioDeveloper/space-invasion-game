import pygame
import src.utils as utils

from pathlib import Path

#Player varaibles
__speed = utils.speed_moviment
player_img = pygame.image.load(Path('assets/foguete.png'))
x_axis = utils.align_center(player_img)
y_axis = 500
x_axis_change = 0

#Bullet Variables
bullet_img = pygame.image.load(Path('assets/bullet.png'))
bullet_x_axis = 0
bullet_y_axis = 500
bullet_y_axis_change = 3
visible_bullet = False

#handler player
def handler(screen: pygame.Surface, x_axis: float):
   x_axis_value = utils.max_value_move_x(player_img)

   #keep inside screen
   if x_axis <= 0 : x_axis = 0
   if x_axis >=  x_axis_value: x_axis = x_axis_value

   screen.blit(player_img, (x_axis, y_axis))

#Handler player moviment
def move(event: pygame.event.Event) -> float:
   x_axis_change = 0
   key_down = event.type == pygame.KEYDOWN
   key_up = event.type == pygame.KEYUP

   # #Move plyer to left or Right
   if (key_down and event.key == pygame.K_LEFT):
      x_axis_change = -__speed

   if (key_down and event.key == pygame.K_RIGHT):
      x_axis_change = __speed

   if (key_up and event.key == pygame.K_LEFT or key_up and event.key == pygame.K_LEFT):
      x_axis_change = 0

   return x_axis_change


#Shoot Bullet
def shoot(screen: pygame.Surface, x, y):
   global visible_bullet
   visible_bullet = True
   screen.blit(bullet_img, (x + 16, y + 10))

# #Shoot Bullet Moviment
# def shoot_moviment(screen: pygame.Surface, x, y):
#    global bullet_visible
#    bullet_visible = True
   
#    screen.blit(bullet_img, (x, y))