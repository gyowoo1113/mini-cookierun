from pico2d import *
import gfw
import gobj
import random

PLAYER_SIZE = 270

class Player:
    RUNNING, FALLING, JUMPING, DOUBLE_JUMP, SLIDING = range(5)
    SLIDE_DURATION = 1.0

    ACTIONS = ['dead', 'doublejump', 'jump', 'slide','run']
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
        self.char = random.choice(['cocoa','yogurt'])
        self.images = Player.load_images(self.char)
        self.action = 'run'
        self.delta = 0, 0

        self.mag = 1
        self.state = Player.RUNNING

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
        self.w, self.h = image.w,image.h

        size = PLAYER_SIZE * self.mag, PLAYER_SIZE * self.mag
#        x,y = 0,0
        flip = 'h' if self.delta[0] < 0 else ''
        image.draw(*self.pos, image.w, image.h)
#        image.clip_draw(x, y, PLAYER_SIZE, PLAYER_SIZE, *self.pos, *size)

    def slide(self):
        if self.state != Player.RUNNING: return
        self.state = Player.SLIDING
        self.action = 'slide'
        self.time = 0.0

    def jump(self):
        if self.action in [Player.FALLING, Player.DOUBLE_JUMP, Player.SLIDING]:
            return
        if self.state == Player.RUNNING:
            self.state = Player.JUMPING
            self.action ='jump'
        elif self.state == Player.JUMPING:
            self.state = Player.DOUBLE_JUMP
            self.action = 'doublejump'
        self.jump_speed = Player.JUMP * self.mag

    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_SPACE or e.key == SDLK_UP:
                self.jump()
            elif e.key == SDLK_DOWN:
                self.slide()

    def get_bb(self):
        x,y = self.pos
        return x - self.w//2, y - self.h//2, x + self.w//2, y + self.h//2

