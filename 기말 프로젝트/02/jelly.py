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
        self.jelly_time =0
        self.images = Jelly.load_images(self.char)

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

