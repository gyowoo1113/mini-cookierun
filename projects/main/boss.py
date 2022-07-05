from pico2d import *
import gfw
import gobj
import random
from jelly import Jelly

class Boss:
    ACTIONS = ['dead', 'sleep', 'wake', 'damage','run','end']
    images = {}
    FPS = 10
    FIDX = 0
    SIZE = {"boss": 0.7}
    def __init__(self,x,y):
        if len(Boss.images) == 0:
            Boss.load_all_images()

        self.x,self.y = x, y
        self.fidx = 0
        self.time = 0
        self.char = 'boss'
        self.images = Boss.load_images(self.char)
        self.action = 'sleep'
        self.delta = 0, 0
        self.speed = 35
        self.power = 100

#        self.w,self.h = 0,0
        self.cnt = 0
        self.size = self.SIZE[self.char]

        self.hit = False
        self.dam = 0
        self.wake = False
        self.score = None

        self.step_sound = load_wav(gobj.RES_DIR + 'sound/boss_step.wav')
        self.step_sound.set_volume(30)
        self.dead_sound = load_wav(gobj.RES_DIR + 'sound/boss_dead.wav')
        self.dead_sound.set_volume(30)
        self.hit_sound = load_wav(gobj.RES_DIR + 'sound/boss.wav')
        self.hit_sound.set_volume(30)
        self.sound = -1
        self.sound_past = -1

    @staticmethod
    def load_all_images():
        Boss.load_images('boss')

    @staticmethod
    def load_images(char):
        if char in Boss.images:
            return Boss.images[char]

        images = {}
        count = 0
        file_fmt = '%s/chaser/%s/%s (%d).png'
        for action in Boss.ACTIONS:
            action_images = []
            n = 0
            while True:
                n += 1
                fn = file_fmt % (gobj.RES_DIR, char, action, n)
                if os.path.isfile(fn):
                    action_images.append(gfw.image.load(fn))
                else:
                    break
                count += 1
            images[action] = action_images
        Boss.images[char] = images
        print('%d images loaded for %s' % (count, char))
        return images

    def update(self):
        self.time += gfw.delta_time

    def draw(self):
        self.fidx = round(self.time * Boss.FPS)
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        big = self.size

        self.w, self.h = image.w/big, image.h/big
        self.change(len(images))
        self.sound = self.fidx % len(images)

        sound = self.sound-self.sound_past

        if self.action =='run' and sound != 0:
            if self.fidx % len(images) == 1:
                self.step_sound.play()

        self.sound_past = self.fidx % len(images)

        image.draw_to_origin(self.x,self.y,self.w, self.h)

    def change(self,img_len):
        Boss.FIDX = self.fidx - self.cnt
        if self.action == 'wake':
            if Boss.FIDX == img_len:
                self.action = 'run'
        if self.action == 'damage':
            if Boss.FIDX == img_len:
                self.action = 'run'
        if self.dam == 5 and self.action != 'dead':
            self.action = 'dead'
            self.cnt = self.fidx
            self.dead_sound.play()
        if self.action == 'dead':
            if Boss.FIDX == img_len:
                gfw.world.remove(self)
        if self.wake:
            if Boss.FIDX >10:
                self.action = 'wake'
                self.cnt = self.fidx
                self.wake = False
        if self.hit:
            self.action = 'end'
            self.cnt = self.fidx
            self.hit = False
        if self.action == 'end':
            if Boss.FIDX == img_len:
                self.action = 'sleep'
                self.dead_sound.play()



    def check(self,item):
        if item.type == 'boss':
            self.action = 'damage'
            self.dam += 1
            self.cnt = self.fidx
            self.score.score += 1000 * self.dam
            self.hit_sound.play()
        elif item.type == 'start':
            self.cnt = self.fidx
            self.wake = True

    def get_bb(self):
        return self.x, self.y, self.x + self.w, self.y + self.h

    def move(self, dx):
        if self.action in ['run']:
            self.x += gfw.delta_time * self.speed
            if self.x > get_canvas_width():
                gfw.world.remove(self)
        elif self.action in ['sleep','damage','end']:
            self.x += dx

        if self.action in ['sleep','end']:
            if self.x + self.w < 0:
                gfw.world.remove(self)

    def check_ui(self):
        if self.score is None:
            if gfw.world.count_at(gfw.layer.score) > 0:
                self.score = gfw.gfw.world.object(gfw.layer.score, 0)


