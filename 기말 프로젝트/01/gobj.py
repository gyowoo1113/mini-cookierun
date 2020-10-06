from pico2d import *

class Cookie:
    def __init__(self,h):
        self.h = h
        self.y = 150
        self.fidx = 0
    def draw(self):
        self.image.clip_draw(self.fidx*100,0,100,self.h,150,self.y)
    def update(self):
        self.y += 0
        self.fidx = (self.fidx+1) % 4
# Cookie 객체의 x값은 고정되어 있음

class Jelly:
    pass
    def draw(self):
        pass
    def update(self):
        pass

#jelly = Jelly()
#jellys = [Jelly() for i in range(12)]      #jelly는 하나로 여러개를 그려야해서

if __name__ == "__main__":
	print("Running test code")