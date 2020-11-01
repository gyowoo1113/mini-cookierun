import random
from pico2d import *
import gfw
import gobj

JELLY_SIZE = 37
# 제일 기본젤리만 만든것
# 이후 자석젤리, 체력, 크기젤리 타입 추가해야함

class Jelly:
    TYPE_1 = range(1)
    def __init__(self, type, x, y):
        self.x, self.y = x, y
        self.image = gfw.image.load(gobj.res('jelly/jelly.png'))
        self.rect = 0,0,37,37
    def update(self): pass
    def draw(self):
        self.image.draw_to_origin(self.x, self.y)
    def move(self, dx):
        self.x += dx
        if self.x + JELLY_SIZE < 0:
            gfw.world.remove(self)
    def get_bb(self):
        return self.x,self.y,self.x+JELLY_SIZE,self.y+JELLY_SIZE

