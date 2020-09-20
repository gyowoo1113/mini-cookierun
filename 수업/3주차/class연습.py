import idleos
#import helper
from pico2d import *
open_canvas()

def handle_events():
    global running
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False

class Grass:
    def __init__(self):
        self.image = load_image('../res/grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self,pos,delta):
        self.x, self.y = pos
        self.dx, self.dy = delta
        self.fidx =0
        self.image = load_image('../res/run_animation.png')
    def draw(self):
        self.image.clip_draw(self.fidx*100,0,100,100,self.x,self.y)
    def update(self):
        self.x+=self.dx
        self.y+=self.dy
        self.fidx=(self.fidx+1)%8

boy = Boy((0,85),(2,0.1))
gra = Grass()

running = True
while running:
    clear_canvas()
    gra.draw()
    boy.draw()
    update_canvas()

    handle_events()

    boy.update()

    if boy.x > get_canvas_width():
        running = False

    delay(0.01)

