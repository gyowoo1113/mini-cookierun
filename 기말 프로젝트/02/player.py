from pico2d import *
import gfw
import gobj
import random
from jelly import Jelly

PLAYER_SIZE = 270

class Player:
    SLIDE_DURATION = 1.0
    ACTIONS = ['dead', 'doublejump', 'jump', 'slide','run','falling']
    GRAVITY = 3000
    JUMP = 1000
    images = {}
    FPS = 10
    FIDX = 0
    SIZE = {'cocoa': 1.2,'yogurt': 1.5}
    BIG = 1
    MAGNET = False
    SUPER = False
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
        self.cookie_time = 0

        self.w,self.h = 0,0
        self.cnt = 0

        self.score = 0
        self.size = self.SIZE[self.char]
        #self.check = -1

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
        if self.action in ['jump','doublejump', 'falling']:
            # print('jump speed:', self.jump_speed)
            self.move((0, self.jump_speed * gfw.delta_time))
            self.jump_speed -= Player.GRAVITY * self.mag * gfw.delta_time

        _,foot,_,_ = self.get_bb()
        if foot < 0:
            self.move((0, get_canvas_height()))
        platform = self.get_platform(foot)
        if platform is not None:
            l,b,r,t = platform.get_bb()
            if self.action in ['run', 'slide']:
                if foot > t:
                    self.action = 'falling'
                    self.jump_speed = 0
            else:
                # print('falling', t, foot)
                if self.jump_speed < 0 and int(foot) <= t:
                    self.move((0, t - foot))
                    self.action = 'run'
                    self.jump_speed = 0
                    # print('Now running', t, foot)
        else:
            self.action = 'falling'
            self.jump_speed = 0
            self.move_down_platform()


    def draw(self):
        self.fidx = round(self.time * Player.FPS)
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        big = self.size*self.mag

        self.w, self.h = image.w/big, image.h/big

        self.change(len(images))

#        size = PLAYER_SIZE * self.mag, PLAYER_SIZE * self.mag
        image.draw_to_origin(*self.pos,self.w, self.h)

    def magnify(self):
        self.mag_speed = 1.0
    def reduce(self):
        self.mag_speed = -1.0

    def slide(self):
        if self.action != 'run': return
        self.action = 'slide'
        self.time = 0.0

    def jump(self):
        if self.action in ['falling','doublejump', 'slide']:
            return
        if self.action == 'run':
            self.action ='jump'
        elif self.action == 'jump':
            self.action = 'doublejump'
            self.cnt = self.fidx
        self.jump_speed = Player.JUMP #* self.mag

    def change(self,img_len):
        Player.FIDX = self.fidx - self.cnt
        if self.action == 'doublejump':
            if Player.FIDX == img_len:
                self.action = 'falling'
        if Player.FIDX > 20.0:
            if self.mag < 1:
                self.reduce()
        elif Player.FIDX > 10.0:
            if self.MAGNET == True:
                self.MAGNET = False

    def check(self,item):
        if item.type == 'jelly':
            self.score += 150
        elif item.type == 'biggest':
            self.cnt = self.fidx
            if self.mag == 1 and self.mag_speed == 0:
                self.magnify()
            self.SUPER = True
        elif item.type == 'magnet':
            self.cnt = self.fidx
            self.MAGNET = True

    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_SPACE or e.key == SDLK_UP:
                self.jump()
            elif e.key == SDLK_DOWN:
                self.slide()
        if e.type == SDL_KEYUP:
            if e.key == SDLK_DOWN:
                if self.action == 'slide':
                    self.cancle()

    def cancle(self):
         if self.action == 'slide':
             self.action = 'run'

    def get_bb(self):
        x,y = self.pos
        return x, y, x + self.w, y + self.h

    def get_platform(self, foot):
        selected = None
        sel_top = 0
        x,y = self.pos
        for platform in gfw.world.objects_at(gfw.layer.platform):
            l,b,r,t = platform.get_bb()
            if x < l or x > r: continue
            mid = (b + t) // 2
            if foot < mid: continue
            if selected is None:
                selected = platform
                sel_top = t
            else:
                if t > sel_top:
                    selected = platform
                    sel_top = t
        # if selected is not None:
        #     print(l,b,r,t, selected)
        return selected
    def move_down_platform(self):
        x,y = self.pos
        y -= 8
        self.pos = x,y
    def update_mag(self):
        if self.mag_speed == 0: return

        self.mag -= self.mag_speed * gfw.delta_time
        if self.mag < 0.75:
            self.mag = 0.75
            self.mag_speed = 0
        elif self.mag > 1.2:
            self.mag = 1.0
            self.mag_speed = 0
            self.SUPER = False

    def move(self, diff):
        self.pos = gobj.point_add(self.pos, diff)

