from pico2d import *
import gfw
import gobj
import random

class Player:
    ACTIONS = ['dead', 'doublejump', 'jump', 'slide','run']
    SLIDE_DURATION = 1.0
    GRAVITY = 3000
    JUMP = 1000
    images = {}
    FPS = 12
    def __init__(self):
        if len(Player.images) == 0:
            Player.load_all_images()

        self.pos = 150, get_canvas_height() // 2
        self.fidx = 0
        self.time = 0
        self.char = random.choice(['cocoa', 'yogurt'])
        self.images = Player.load_images(self.char)
        self.action = 'run'
        self.delta = 0, 0


    @staticmethod
    def load_all_images():
        Player.load_images('cocoa')
        Player.load_images('yogurt')

    @staticmethod
    def load_images(char):
        if char in Player.images:
            return Player.images[char]

        images = {}
        count = 0
        file_fmt = '%s/cookie/%s/%s (%d).png'
        for action in Player.ACTIONS:
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
        Player.images[char] = images
        print('%d images loaded for %s' % (count, char))
        return images

    def update(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * Player.FPS)

    def draw(self):
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        flip = 'h' if self.delta[0] < 0 else ''
        image.draw(*self.pos, image.w//1.5, image.h//1.5)
