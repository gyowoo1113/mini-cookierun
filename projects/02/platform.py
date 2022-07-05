import random
from pico2d import *
import gfw
import gobj

UNIT = 20
INFO = [
    (6.5 * UNIT, 2 * UNIT, 'map_obj/bottom_01.png'),
#    (6 * UNIT, 7 * UNIT, 'map_obj/bottom_02.png'),
    (6 * UNIT, 7 * UNIT, 'map_obj/bottom_03.png'),
]

class Platform:
    T_6x2, T_6x7 = range(2)
    SIZES = [ (6,2), (6,7) ]
    def __init__(self, type, left, bottom):
        self.left = left
        self.bottom = bottom
        #self.can_pass = type >= Platform.T_6x7
        self.width, self.height, fn = INFO[type]
        self.image = gfw.image.load(gobj.res(fn))
    def update(self): pass
    def draw(self):
        self.image.draw_to_origin(self.left, self.bottom, self.width, self.height)
    def get_bb(self):
        return self.left, self.bottom, self.left + self.width, self.bottom + self.height
    def move(self, dx):
        self.left += dx
        if self.left + self.width < 0:
            # print('count was:', gfw.world.count_at(gfw.layer.platform))
            gfw.world.remove(self)
    @property
    def right(self):
        return self.left + self.width