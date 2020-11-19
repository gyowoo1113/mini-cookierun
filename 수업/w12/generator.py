from pico2d import *
import gfw
from missile import Missile
import random

MISSILE_COUNT = 10

def init():
    pass

def update():
    while gfw.world.count_at(gfw.layer.missile) < MISSILE_COUNT:
        generate()

def generate():
    x,y,dx,dy =get_coords()
    m = Missile((x,y),(dx,dy))
    gfw.world.add(gfw.layer.missile,m)

def get_coords():
    x = random.randrange(get_canvas_width())
    y = random.randrange(get_canvas_height())
    dx = random.random()
    if dx < 0.5: dx-=1
    dy = random.random()
    if dy < 0.5: dy-=1
    side = random.randint(1,4)
    if side == 1: #left
        x = 0
    elif side == 2: #bottom
        y = 0
    elif side == 3: # right
        x = get_canvas_width()
    else:
        y = get_canvas_height()

    return x,y,dx,dy

