import pygame
import src.player as player

screen_with = 800
screen_height = 800
x_change = 0

# initialize game
pygame.init()

pygame.display.set_caption("Space Invasion")
screen = pygame.display.set_mode((800, 600))

running = True
while running:
   screen.fill("purple")

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False

      if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
         x_change = player.move(event)

   #Change player location
   player.x += x_change
   player.handler(screen, player.x)

   pygame.display.update()
