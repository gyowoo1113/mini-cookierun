from pico2d import *
import gfw
from gobj import *

class Score:
    def __init__(self, x, y,color,size):
        self.x, self.y = x, y
        self.font = load_font(RES_DIR + 'font/CookieRun Regular.ttf',size)
        self.color = color
        self.reset()

    def reset(self):
        self.score = 0
        self.display = 0

    def draw(self):
        self.font.draw(self.x,self.y,'%d' % self.display,self.color)

    def update(self):
        if self.display < self.score:
            self.display += 50
            if self.display > self.score:
                self.display = self.score
