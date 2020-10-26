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
    FPS = 10
    def __init__(self):
        if len(Player.images) == 0:
            Player.load_all_images()

        self.pos = 150, get_canvas_height() // 2- 150
        self.fidx = 0
        self.time = 0
        self.char = random.choice(['cocoa','yogurt'])
        self.images = Player.load_images(self.char)
        self.action = 'run'
        self.delta = 0, 0

        self.mag = 1
        self.mag_speed = 0
        self.state = Player.RUNNING
        self.cookie_time = 0

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

        self.update_mag()
        self.cookie_time += gfw.delta_time
        self.time += gfw.delta_time
        if self.state in [Player.JUMPING, Player.DOUBLE_JUMP, Player.FALLING]:
            # print('jump speed:', self.jump_speed)
            self.move((0, self.jump_speed * gfw.delta_time))
            self.jump_speed -= Player.GRAVITY * self.mag * gfw.delta_time

    def update_mag(self):
        if self.mag_speed == 0: return

        x,y = self.pos
        _,b,_,_ = self.get_bb()
        diff = y - b
        prev_mag = self.mag

        self.mag += self.mag_speed * gfw.delta_time
        if self.mag > 2.0:
            self.mag = 2.0
            self.mag_speed = 0
        elif self.mag < 1.0:
            self.mag = 1.0
            self.mag_speed = 0

        new_y = b + diff * self.mag / prev_mag
        self.pos = x,new_y

    def move(self, diff):
        self.pos = gobj.point_add(self.pos, diff)

    def draw(self):
        self.fidx = round(self.time * Player.FPS)
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        self.w, self.h = image.w,image.h

        size = PLAYER_SIZE * self.mag, PLAYER_SIZE * self.mag
        flip = 'h' if self.delta[0] < 0 else ''
        image.draw_to_origin(*self.pos,self.w, self.h)

#        image.draw(*self.pos, image.w, image.h)
#        x,y = 0,0
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
        if e.type == SDL_KEYUP:
            if e.key == SDLK_DOWN:
                if self.state == Player.SLIDING:
                    self.cancle()

    def cancle(self):
         if self.state == Player.SLIDING:
             self.state = Player.RUNNING
             self.action = 'run'

    def get_bb(self):
        x,y = self.pos
        return x, y, x + self.w, y + self.h

