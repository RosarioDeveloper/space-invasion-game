import pygame

screen_with = 800
screen_height = 800


#initialize game
pygame.init()

pygame.display.set_caption("Space Invasion")
screen = pygame.display.set_mode((800, 600))
running = True

img_player = pygame.image.load('./assets/foguete.png')
player_x = (screen_with / 2) - (img_player.get_width() / 2)
player_y = 536

def player(x, y):
   screen.blit(img_player, (x, y))

while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT :  running = False

   #Fill background
   screen.fill("purple")

   player_x += 0.1
   player(player_x, player_y)

   pygame.display.update()
