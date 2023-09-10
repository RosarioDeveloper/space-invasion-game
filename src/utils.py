
from pygame import Surface
from src.config import config

def max_value_to_move_x(img: Surface) -> float:
   return (config.screen_with - img.get_width())