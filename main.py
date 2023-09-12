import pygame
import math
import random
import src.player as player
import src.enemy as enemy

import src.utils as utils


#Constants
WHITE = (255, 255, 255)
BLACK = (0,0,0)

# initialize game
pygame.init()
pygame.display.set_caption("Space Invasion")
screen = pygame.display.set_mode((utils.screen_with, utils.screen_height))
background = pygame.image.load("./assets/background.jpg")

# Add Music
pygame.mixer.music.load("./assets/audio/background_music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#Variables
restart_button = utils.get_font(20).render("Start game", True, WHITE)
restart_button_align = restart_button.get_rect()
restart_button_align.center = (utils.screen_with // 2, 500)

score = 0
score_font = utils.get_font(30)

#Score
def handler_score():
   text = score_font.render(f'Score: {score}', True, WHITE)
   screen.blit(text, (10, 10))

#Detect Collosion
def there_is_collision(x1: float, y1: float, x2: float, y2: float) -> bool:
   distance = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y2 -y1), 2))
   return True if distance < 27 else False


#End of the game
is_game_over = False
game_over_font = pygame.font.Font("freesansbold.ttf", 40)
def game_over():
   text = game_over_font.render("GAME OVER", True, WHITE)
   pygame.mixer.music.stop()

   screen.blit(text, (utils.align_center(text), 250))
   screen.blit(restart_button, restart_button_align)

   
#Close Event
def close_game(event: pygame.event.Event):
   global running
   if event.type == pygame.QUIT:  running = False

#Restart game
def restart_game(event: pygame.event.Event):
   global is_game_over

   if event.type == pygame.MOUSEBUTTONDOWN:
      if restart_button_align.collidepoint(event.pos):
         is_game_over = False

         pygame.mixer.music.load("./assets/audio/background_music.mp3")
         pygame.mixer.music.set_volume(0.5)
         pygame.mixer.music.play(-1)

         #Restat enemies position
         for k in range(enemy.numer_0f_enemies):
            enemy.y_axis[k] = random.randint(0, 200)


#Start Game
def start_game():
   global is_game_over, score, running

   for event in pygame.event.get():
      #Closing Event
      close_game(event)

      # Process key event   
      if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
         player.x_axis_change = player.move(event)

      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
         if not (player.visible_bullet):
            bullet_sound = pygame.mixer.Sound("./assets/audio/shot.mp3")
            bullet_sound.play()

            player.bullet_x_axis = player.x_axis
            player.shoot(screen, player.bullet_x_axis, player.bullet_y_axis)
            
   #Change player location
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
      #End of game
      is_game_over = enemy.y_axis[en] > 400

      if(is_game_over): 
         for k in range(enemy.numer_0f_enemies):
            enemy.y_axis[k] = 1000
         break
         
      enemy.x_axis[en] += enemy.x_axis_change[en]
      
      #Collision
      collesion = there_is_collision(
         enemy.x_axis[en], enemy.y_axis[en], player.bullet_x_axis, player.bullet_y_axis
      )

      if(collesion):
         collision_sound = pygame.mixer.Sound("./assets/audio/punch.mp3")
         collision_sound.play()

         #Restart bullet position
         player.bullet_y_axis = 500
         player.visible_bullet = False

         #Count Scores
         score += 1

         #Restart enemy position
         enemy.x_axis[en] = random.randint(0, int(enemy.max_value_move_x))
         enemy.y_axis[en] = random.randint(0, 200)

      enemy.handler(screen, enemy.x_axis[en], en)

   player.handler(screen, player.x_axis)
   handler_score()



#Run Game
running = True
while running:
   #Background
   screen.blit(background, (0,0))
   
   if(is_game_over):
      for event in pygame.event.get(): restart_game(event)
      game_over()
   else:
      start_game()

   pygame.display.flip()

pygame.quit()