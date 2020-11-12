from pico2d import *
import gfw
import gobj

class Life():
    def __init__(self):
        self.height = get_canvas_height() - 50
        self.width = get_canvas_width()/2
        self.bg = gfw.image.load(gobj.RES_DIR + 'ui/heart/gauge_bg.png')
        self.fg = gfw.image.load(gobj.RES_DIR + 'ui/heart/gauge_fg.png')
        self.icon = gfw.image.load(gobj.RES_DIR + 'ui/heart/heart_icon.png')
        self.effect = gfw.image.load(gobj.RES_DIR + 'ui/heart/effect.png')
        self.life = self.width

    def draw(self):
        self.bg.draw_to_origin(self.width/2, self.height, self.width, self.bg.h)
        self.fg.clip_draw_to_origin(0, 0, int(self.life), self.fg.h,
                                    self.width/2, self.height,self.life, self.fg.h)
        self.icon.draw_to_origin(self.width/2-self.icon.w+10, self.height-8)
        self.effect.draw_to_origin(self.width/2+int(self.life)-12, self.height-11,
                                   self.effect.w,50)

    def enter(self):
        pass
    def update(self):
        pass
