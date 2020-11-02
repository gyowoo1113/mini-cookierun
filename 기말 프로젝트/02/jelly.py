import random
from pico2d import *
import gfw
import gobj

JELLY_SIZE = 37
# 제일 기본젤리만 만든것
# 이후 자석젤리, 체력, 크기젤리 타입 추가해야함

class Jelly:
    images = {}
    TYPES = ['jelly','magnet', 'bonus', 'boss', 'speed','biggest']
    FPS = 5

    def __init__(self, type, x, y):
        if len(Jelly.images) == 0:
            Jelly.load_all_images()

        self.x, self.y = x, y
        self.rect = 0,0,37,37

        self.type = type
        self.fidx = 0
        self.time = 0
        self.char = 'jelly'
        self.speed = 300
        self.jelly_time =0
        self.images = Jelly.load_images(self.char)
        if gfw.world.count_at(gfw.layer.player) > 0:
            self.player = gfw.world.object(gfw.layer.player, 0)

        #self.target= 0
        #self.delta = 0

    @staticmethod
    def load_all_images():
        Jelly.load_images('jelly')

    @staticmethod
    def load_images(char):
        if char in Jelly.images:
            return Jelly.images[char]

        images = {}
        count = 0
        file_fmt = '%s/%s/%s (%d).png'
        for type in Jelly.TYPES:
            type_images = []
            n = 0
            while True:
                n += 1
                fn = file_fmt % (gobj.RES_DIR,char, type, n)
                if os.path.isfile(fn):
                    type_images.append(gfw.image.load(fn))
                else:
                    break
                count += 1
            images[type] = type_images
        Jelly.images[char] = images
        print('%d images loaded for %s' % (count, char))
        return images

    def update(self):
        self.jelly_time += gfw.delta_time
        self.time += gfw.delta_time
        if self.player.MAGNET == True:
            self.move_to_player()

    def draw(self):
        self.fidx = round(self.time * Jelly.FPS)
        images = self.images[self.type]
        image = images[self.fidx % len(images)]
        #이미지 사이즈 조절 시 수정필요
        self.w, self.h = image.w,image.h

        image.draw_to_origin(self.x, self.y)

    def move(self, dx):
        self.x += dx
        if self.x + JELLY_SIZE < 0:
            gfw.world.remove(self)

    def get_bb(self):
        return self.x,self.y,self.x+self.w,self.y+ self.h

    def update_position(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * Jelly.FPS)

        x,y = self.x,self.y
        dx,dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time

        # print(self.pos, self.delta, self.target, x, y, dx, dy)

        tx,ty = self.target
        if dx > 0 and x >= tx or dx < 0 and x <= tx:
            x = tx
            done = True
        if dy > 0 and y >= ty or dy < 0 and y <= ty:
            y = ty
            done = True

        self.x,self.y = x,y

    def move_to_player(self):
        self.set_target(self.player.pos)
        self.update_position()
        #collides = gobj.collides_box(self, self.player)

    def set_target(self, target):
        x,y = self.x,self.y
        tx,ty = target
        dx, dy = tx - x, ty - y
        distance = math.sqrt(dx**2 + dy**2)
        if distance == 0: return

        self.target = target
        self.delta = dx / distance, dy / distance

