from pygame import Surface

screen_with = 800
screen_height = 600

def max_value_move_x(img: Surface) -> float:
   return (screen_with - img.get_width())

#Calc the center element position
def center_position(el: Surface) -> float:
   return (screen_with / 2) - (el.get_width() / 2)
