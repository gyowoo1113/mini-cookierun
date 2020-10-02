from pico2d import *
open_canvas()
# 01 - 180,200  02 - 170,224  03-190,256

def handle_events():
    global running
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif (e.type,e.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
            running = False

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

cookie = Cookie((180,200),4,180)
cookie.image = load_image('../res/cookie/cookie01_run.png')
#jelly = Jelly()
#jellys = [Jelly() for i in range(12)]      #jelly는 하나로 여러개를 그려야해서
#jelly 동작시켜 보고 따로 떼놓아야함

running = True
while running:
    clear_canvas()

    cookie.draw()
#    for jelly in jellys:
#        jelly.draw()

    update_canvas()
    handle_events()

    cookie.update()
    get_events()

    delay(0.05)

close_canvas()
