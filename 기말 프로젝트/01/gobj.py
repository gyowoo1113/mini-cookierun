from pico2d import *
import gfw


class Cookie:
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    KEYDOWN_DOWN = (SDL_KEYDOWN,SDLK_DOWN)

    def __init__(self,h):
        self.h = h
        self.y = 100
        self.fidx = 0
        self.sizx,self.sizy = [100,h]
        self.jump = False
        self.ReadyJP = False
        self.cnt=0
    def draw(self):
        if(self.jump):
            self.image2.clip_draw(self.fidx*100,0,100,self.h,125,self.y,self.sizx,self.sizy)
        else:
            self.image.clip_draw(self.fidx*100,0,100,self.h,150,self.y,self.sizx,self.sizy)
    def update(self):
        if self.jump:
            if self.ReadyJP:
                self.fidx = 0
                if self.cnt == 3:
                    self.ReadyJP = False
            else:
                self.fidx = 1

            self.cnt += 1
            if self.cnt == 12:
                self.jump = False
        else:
            self.fidx = (self.fidx+1) % 4
    def Jump(self):
        self.ReadyJP = True
        self.jump = True
        self.cnt=0
    def down(self):
        pass
    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair == Cookie.KEYDOWN_SPACE:
            self.Jump()
        elif pair == Cookie.KEYDOWN_DOWN:
            self.down()
#sep 25

class Back:
    def __init__(self,dx):
        self.fidx = 0
        self.dx = dx
        self.w,self.h = [1075,400]
        self.y,self.sh = [200,400]
    def draw(self):
        self.image.clip_draw(self.fidx,0,self.w,self.h,400-self.fidx*2,self.y,800,self.sh)
        self.image.clip_draw(0,0,self.w,self.h,1200-self.fidx*2,self.y,800,self.sh)
    def update(self):
        self.fidx += self.dx

        if(800-self.fidx*2 <0):
            self.fidx=0

class Bottom:
    pass
    def draw(self):
        pass
    def update(self):
        pass

class Jelly:
    pass
    def draw(self):
        pass
    def update(self):
        pass



if __name__ == "__main__":
	print("Running test code")