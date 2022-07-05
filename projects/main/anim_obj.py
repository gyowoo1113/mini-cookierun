import random
from pico2d import *
import gfw
import gobj

class AnimObject:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.images = []
        self.fps = 1
        self.time = 0
        self.loops = False
        self.w,self.h = 0,0
        self.crash = False
        self.rad = 0
        self.speed = 1000

    def set_anim(self, files, fps, loops):
        self.images = [gfw.image.load(f) for f in files ]
        if len(self.images) > 0:
            self.image = self.images[0]
        self.fps = fps
        self.loops = loops

    def pass_wh(self,w,h):
        self.w,self.h = w,h

    def update(self):
        image_count = len(self.images)
        if image_count <= 1: return
        self.time += gfw.delta_time
        fidx = round(self.time * self.fps)
        if self.loops:
            fidx %= image_count
        elif fidx >= image_count:
            fidx = image_count - 1
        self.image = self.images[fidx]
        # print(fidx)

        width, height = get_canvas_width(), get_canvas_height()
        width += 100
        height /= 2

        if self.crash:
            self.rad += 12
            self.move_to_pos((width,height))

    def draw(self):
        if self.crash:
            self.image.clip_composite_draw(0,0,self.image.w,self.image.h,self.rad,'',self.x,self.y,self.w,self.h)
        else:
            self.image.draw_to_origin(self.x, self.y,self.w,self.h)

    def move(self, dx):
        self.x += dx

        if self.crash:
            if self.x > get_canvas_width():
                gfw.world.remove(self)
        else:
            if self.x + self.image.w < 0:
                gfw.world.remove(self)

    def update_position(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * self.fps)

        x,y = self.x,self.y
        dx,dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time

        tx,ty = self.target
        if dx > 0 and x >= tx or dx < 0 and x <= tx:
            x = tx
            done = True
        if dy > 0 and y >= ty or dy < 0 and y <= ty:
            y = ty
            done = True

        self.x,self.y = x,y

    def move_to_pos(self,pos):
        self.set_target(pos)
        self.update_position()

    def set_target(self, target):
        x,y = self.x,self.y
        tx,ty = target
        dx, dy = tx - x, ty - y
        distance = math.sqrt(dx**2 + dy**2)
        if distance == 0: return

        self.target = target
        self.delta = dx / distance, dy / distance

