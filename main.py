import pygame
import random

# initialize game
pygame.init()
pygame.mixer.init()

#Defines Colors
WHITE = (255, 255, 255)
LIGHT = (192, 192, 192)
RED = (255, 81, 123)
RED_80 = (255, 171, 186)
GREEN = (173, 255, 0)
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
font15 = pygame.font.Font(font_type,15)
font20 = pygame.font.Font(font_type,20)
font40 = pygame.font.Font(font_type,40)

# Define Sound
shot_sound = pygame.mixer.Sound("./assets/sounds/shot.mp3")
shot_sound.set_volume(0.5)

explosion_sound1 = pygame.mixer.Sound("./assets/sounds/explosion.wav")
explosion_sound1.set_volume(0.5)
explosion_sound2 = pygame.mixer.Sound("./assets/sounds/explosion2.wav")
explosion_sound2.set_volume(0.5)

#Game Variables
enemy_rows = 3
enemy_cols = 7
total_enemies = enemy_cols * enemy_rows
scores = 0
game_started = False
game_won = 0
time_gameover = 2
last_time = pygame.time.get_ticks()
enemy_and_player_collision = False

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


   def shot(self):
      current_time = pygame.time.get_ticks()
      interval = 500 #millseconds

      if current_time - self.time_shot > interval:
         shot_sound.play()
         player_bullet_group.add(Player_Bullet(self.rect.centerx + 4.5, self.rect.y))
         self.time_shot = current_time


#Create Bullet Class
class Player_Bullet(pygame.sprite.Sprite):
   def __init__(self, x, y) :
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load('./assets/images/bullet.png')
      self.rect = self.image.get_rect()
      self.rect.center = (x, y)

   def update(self):
      global scores, game_won
      self.rect.y -= 5

      if self.rect.bottom < 0:
         self.kill()

      #Detect Enemy collision
      if pygame.sprite.spritecollide(self, enemy_group, True):
         scores = total_enemies - len(enemy_group)
         explosion_group.add(Explosion(self.rect.x, self.rect.y, 4))
         explosion_sound2.play()
         self.kill()

      #Detect Enemy bullet collision
      if pygame.sprite.spritecollide(self, enemy_bullet_group, True):
         self.kill()


# Enemy Bullets
class Enemy_Bullet(pygame.sprite.Sprite):
   def __init__(self, x: int, y: int):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load(f'./assets/images/enemy_bullet.png')
      self.rect = self.image.get_rect()
      self.rect.center = (x, y)
      
   def update(self):
      global game_won, time_gameover
      self.rect.y += 2

      #Detect Player collision
      if pygame.sprite.spritecollide(self, player_group, True):
         self.kill()
         explosion_sound1.play()
         explosion_group.add(Explosion(self.rect.x, self.rect.y, 8))
         
         #Time to game over
         time_gameover = 2

      if self.rect.y > screen_height:
         self.kill()


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
      self.shot_interval = abs(random.randint(2000, 5000))
      self.current_index = 0


   def update(self):
      global game_won, time_gameover
      self.rect.x += self.move_x
      self.move_x_count += 1

      #Stop Process
      if(self.rect.y > screen_height):
         self.kill()
      
      # Calculate Left and Right movement
      if abs(self.move_x_count) > 75:
         self.move_x *= -1
         self.move_x_count *= self.move_x
         self.rect.y += 15

      
      #Shot
      current_time = pygame.time.get_ticks()
      numer_enemy_attacking = len(enemy_bullet_group) < 5 and len(enemy_group) > 0
      if current_time - self.time_shot > self.shot_interval and numer_enemy_attacking:
         self.shot(current_time)

      
      #Detect game over
      if self.rect.bottom > screen_height - 50:
         self.kill()
         
         if len(player_group) > 0:
            explosion_sound1.play()
            player = random.choice(player_group.sprites())
            explosion_group.add(Explosion(player.rect.x, player.rect.y, 8))
            explosion_sound1.play()
            
            player.kill()
         
            #Time to game over
            time_gameover = 2


   def shot(self,current_time: int): 
      enemy_bullet_group.add(Enemy_Bullet(self.rect.centerx, self.rect.bottom + 30))
      self.time_shot = current_time


#Explosion
class Explosion(pygame.sprite.Sprite):
   def __init__(self, x, y, size: int) -> None:
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load('./assets/images/exp1.png')
      self.rect = self.image.get_rect()
      self.rect.center = (x, y)
      self.counter = 0
      self.index = 0
      self.size = size
      self.counter = 0

   
   def update(self):
      self.counter += 1
      speed = 2


      if self.counter >= speed and self.index < 5:
         self.index += 1
         self.counter = 0
         img = pygame.image.load(f'./assets/images/exp{self.index}.png')
         self.image = pygame.transform.scale(img, (self.size * 10, self.size * 10))

      if(self.index >= 5):
         self.kill()
   

# Define Sprites Groups
player_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()

# Create player
player_group.add(Player(screen_center, screen_height - 50))


#Functions
def draw_text(text, color, font: pygame.font.Font, x , y):
   text_font = font.render(text, True, color)
   screen.blit(text_font, (x - text_font.get_width() / 2, y))

def draw_image(path,  x , y):
   image = pygame.image.load(path)
   screen.blit(image, (x - image.get_width() / 2, y))


def create_enemies():
   for row in range(enemy_rows):
      for col in range(enemy_cols):
         enemy = Enemy(100 + col * 100, 100 + row * 70)
         enemy_group.add(enemy)

# Restart Game
def restart_game(key):
   global game_won, scores, enemy_and_player_collision

   enemy_and_player_collision = False
   enemy_group.empty()
   enemy_bullet_group.empty()
   player_bullet_group.empty()
   player_group.empty()
   explosion_group.empty()

   #Restart Game
   if key[pygame.K_f]:
      game_won = 0
      scores = 0
      create_enemies()
      player_group.add(Player(screen_center, screen_height - 50))


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
   
   #Calculate time to game over
   if time_gameover > 0:
      count_timer = pygame.time.get_ticks()
      if count_timer - last_time > 1000:
         time_gameover -= 1
         last_time = count_timer

   #Start Game
   keys = pygame.key.get_pressed()
   if keys[pygame.K_RETURN]:
      game_started = True
      scores = 0

   #Start game
   if not game_started:
      draw_image('./assets/images/start_screen_design.png', screen_center, 100)
      draw_text("PRESS 'ENTER TO START", LIGHT, font15, screen_center, 330)

   if game_started:

      #Player Lose
      if game_won < 0:
         draw_image('./assets/images/you_lose.png', screen_center, 100)
         draw_text(f'SCORE: {scores}  BEST: {scores}', GREEN, font20, screen_center, 220)
         draw_text("PRESS 'F' TO RESTART", LIGHT, font15, screen_center, 300)

         #Restart Game
         restart_game(keys)

      #Player Won
      if game_won == 1 and len(enemy_group) == 0:
         draw_image('./assets/images/victory_design.png', screen_center, 100)
         draw_text("PRESS 'F' TO PLAY AGAIN", LIGHT, font15, screen_center, 300)

         #Restart Game
         restart_game(keys)
      
      #Draw Elements
      if game_won == 0 :
         draw_text(f'Score: {scores}', LIGHT, font10, screen_center + 10, 10)

         if time_gameover == 0:

            #Detect Game ver
            if len(player_group) == 0:
               game_won = -1

         #Player Win
         if scores >= enemy_cols * enemy_rows:
            game_won = 1
      
         enemy_bullet_group.update()
         enemy_group.update()
         player_bullet_group.update()
         player_group.update()
         explosion_group.update()
      
      enemy_bullet_group.draw(screen)
      enemy_group.draw(screen)
      explosion_group.draw(screen)
      player_bullet_group.draw(screen)
      player_group.draw(screen)

   pygame.display.update()

pygame.quit()