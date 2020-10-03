from pico2d import *

class Cookie:
    def __init__(self,pos,fidxNum,y):
        self.w , self.h = pos
        self.fidxNum = fidxNum
        self.y = y
        self.fidx = 0
    def draw(self):
        self.image.clip_draw(self.fidx*self.w,0,self.w,self.h,100,self.y)
    def update(self):
        self.y += 0
        self.fidx = (self.fidx+1) % self.fidxNum
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