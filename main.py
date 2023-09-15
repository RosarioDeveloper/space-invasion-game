from typing import Any
import pygame
import random

# initialize game
pygame.init()
pygame.mixer.init()

#Defines Colors
WHITE = (255, 255, 255)
LIGHT = (192, 192, 192)
RED = (255, 171, 186)
GREEN = (153, 255, 201)
BLACK = (0,0,0)

#Define fps
clock = pygame.time.Clock()
fps = 60

screen_with = 800
screen_height = 600
screen_center = screen_with / 2

pygame.display.set_caption("Space Invasion")
screen = pygame.display.set_mode((screen_with, screen_height))
background = pygame.image.load("./assets/images/background.png")

#Define fonts
font_type = "./assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf"
font10 = pygame.font.Font(font_type,10)

# Define Sound
shot_sound = pygame.mixer.Sound("./assets/sounds/shot.mp3")
shot_sound.set_volume(0.5)

explosion_sound = pygame.mixer.Sound("./assets/sounds/explosion2.wav")
explosion_sound.set_volume(0.5)

#Game Variables
enemy_rows = 3
enemy_cols = 7
scores = 0


def draw_text(text, color, font: pygame.font.Font, x , y):
   text_font = font.render(text, True, color)
   screen.blit(text_font, (x, y))


# Create Player Class
class Player(pygame.sprite.Sprite):
   def __init__(self, x, y) :
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load('./assets/images/player.png')
      self.rect = self.image.get_rect()
      self.rect.center = (x, y)
      self.time_shot = pygame.time.get_ticks()

   def update(self):
      speed = 8
      
      #Key Press
      key = pygame.key.get_pressed()
      if key[pygame.K_LEFT] and self.rect.left > 0:
         self.rect.x -= speed
      if key[pygame.K_RIGHT] and self.rect.right < screen_with:
         self.rect.x += speed

      #Shot Bullet
      if(key[pygame.K_SPACE]):
         self.shot()

      #Drow health bar
      # pygame.draw.rect(
      #    screen, 
      #    RED, 
      #    (self.rect.x, (self.rect.bottom), self.rect.width, 5)
      # )

   def shot(self):
      current_time = pygame.time.get_ticks()
      interval = 500 #millseconds

      if current_time - self.time_shot > interval:
         shot_sound.play()
         bullet_group.add(Bullet(self.rect.centerx + 4.5, self.rect.y))
         self.time_shot = current_time



#Create Bullet Class
class Bullet(pygame.sprite.Sprite):
   def __init__(self, x, y) :
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load('./assets/images/bullet2.png')
      self.rect = self.image.get_rect()
      self.rect.center = (x, y)

   def update(self):
      global scores
      self.rect.y -= 5

      if self.rect.bottom < 0:
         self.kill()

      #Detect Enemy collision
      if pygame.sprite.spritecollide(self, enemy_group, True):
         self.kill()
         scores += 1
         explosion_sound.play()


# Enemy Class
class Enemy(pygame.sprite.Sprite):
   def __init__(self, x, y) :
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load(f'./assets/images/enemy_{str(random.randint(1,2))}.png')
      self.rect = self.image.get_rect()
      self.rect.center = (x, y)
      self.time_shot = pygame.time.get_ticks()
      self.move_x_count = 1
      self.move_x = 1

   def update(self):
      self.rect.x += self.move_x
      self.move_x_count += 1
      
      # Calculate Left and Right movement
      if abs(self.move_x_count) > 75:
         self.move_x *= -1
         self.move_x_count *= self.move_x
         self.rect.y += 10

      #Stop Process
      if(self.rect.y > screen_height):
         self.kill()
            
      




# Define Sprites Groups
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# Create player
player_group.add(Player(screen_center, screen_height - 50))


#Functions
def create_enemies():
   for row in range(enemy_rows):
      for col in range(enemy_cols):
         enemy_group.add(Enemy(100 + col * 100, 100 + row * 70))


create_enemies()

#Run Game
running = True
while running:
   clock.tick(fps)

   #Draw Background
   screen.blit(background, (0,0))

   for event in pygame.event.get():
      if(event.type == pygame.QUIT):
         running = False

   #Draw Scores
   draw_text(f'Score: {scores}', LIGHT, font10, screen_center - 30, 10)

   #Handler Enemy
   enemy_group.draw(screen)
   enemy_group.update()

   #Handler Bullet
   bullet_group.draw(screen)
   bullet_group.update()

   #Handler Player
   player_group.update()
   player_group.draw(screen)

   pygame.display.update()

pygame.quit()