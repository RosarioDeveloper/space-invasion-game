from pygame import Surface, font

screen_with = 800
screen_height = 600
speed_moviment = 0.5

def max_value_move_x(img: Surface) -> float:
   return (screen_with - img.get_width())

#Calc the center element position
def align_center(el: Surface) -> float:
   return (screen_with / 2) - (el.get_width() / 2)

def get_font(size: int = 20) -> font.Font:
   return font.Font("freesansbold.ttf", size)