import pygame
from pathlib import Path

img_player = pygame.image.load(Path('assets/foguete.png'))

def player(screen: pygame.Surface, x: float):
   screen.blit(img_player, (x, 536))