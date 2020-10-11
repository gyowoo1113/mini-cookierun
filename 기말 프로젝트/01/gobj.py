from pico2d import *

class Cookie:
    def __init__(self,h):
        self.h = h
        self.y = 110
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

class Back:
    def __init__(self,w,h,dx,y):
        self.fidx = 0
        self.dx = dx
        self.w = w
        self.h = h
        self.y = y
        self.x = 0
        self.fidw = 0
    def draw(self):
        self.image.clip_draw(self.fidx,0,self.w,self.h,537.5-self.x*2,self.y)
        self.image.clip_draw(0,0,int(self.x*2),self.h,1075-self.x,self.y)
    def update(self):
        self.fidx += self.dx
        self.fidw = self.fidx*(800/self.w)
        self.x = self.fidx*(self.w/800)

        if(1075-self.x*2 <0):
            self.fidx=0

#jelly = Jelly()
#jellys = [Jelly() for i in range(12)]      #jelly는 하나로 여러개를 그려야해서

if __name__ == "__main__":
	print("Running test code")