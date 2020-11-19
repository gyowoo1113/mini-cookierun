from pico2d import *
import gfw

MOVE_PPS = 200
class Missile:
    def __init__(self,pos,delta):
        self.pos = pos
        self.delta = delta
        self.image = gfw.image.load('res/missile.png')
        self.radius = self.image.w // 2
        self.bb_l = -self.image.w
        self.bb_b = -self.image.h
        self.bb_r = get_canvas_width() + self.image.w
        self.bb_t = get_canvas_height() + self.image.h
    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx * MOVE_PPS * gfw.delta_time
        y += dy * MOVE_PPS * gfw.delta_time
        self.pos = x,y
        if self.out_of_screen():
            gfw.world.remove(self)
    def draw(self):
        self.image.draw(*self.pos)
    def out_of_screen(self):
        x,y = self.pos
        if x < self.bb_l: return True
        if x > self.bb_r: return True
        if y < self.bb_b: return True
        if y > self.bb_t: return True

        return False

