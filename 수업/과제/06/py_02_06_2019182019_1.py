import helper
from pico2d import *
open_canvas()

num,cnt=[0,0]
tx =[]
ty =[]

def set_target(obj,target):
    obj.target = target
    obj.delta = [0,0] if target is None else helper.delta(obj.pos, target, obj.speed)

def move_toward_obj(obj):
    global num,cnt
    if obj.target == None: return
    pos, done = helper.move_toward(obj.pos, obj.delta, obj.target)
    if done:
        obj.speed = 1
        obj.delta = 0,0
        if(cnt != num):
         set_target(boy,(tx[num],ty[num]))
         num+=1
        else:
            obj.target = None
    obj.pos = list(pos)

def handle_events():
    global running
    global boy
    global tx,ty
    global num,cnt
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False
        elif e.type == SDL_MOUSEBUTTONDOWN and boy.target== None:
            tx.append(e.x), ty.append(600-1-e.y)
            set_target(boy,(tx[num],ty[num]))
            boy.delta = list(helper.delta(boy.pos,(tx[num],ty[num]),boy.speed))
            num += 1
            cnt += 1
        elif e.type == SDL_MOUSEBUTTONDOWN and boy.target!= None:
            boy.speed+=3
            boy.delta = list(helper.delta(boy.pos,boy.target, boy.speed))
            tx.append(e.x), ty.append(600-1-e.y)
            cnt += 1

class Grass:
    def __init__(self):
        self.image = load_image('../res/grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.target=None
        self.pos = [400,85]
        self.speed = 1
        self.delta = [0,0]
        self.fidx =0
        self.image = load_image('../res/run_animation.png')
    def draw(self):
        self.image.clip_draw(self.fidx*100,0,100,100,self.pos[0],self.pos[1])
    def update(self):
        self.pos[0]+=self.delta[0]
        self.pos[1]+=self.delta[1]
        self.fidx=(self.fidx+1)%8

boy = Boy()
gra = Grass()

running = True
while running:
    clear_canvas()
    gra.draw()
    boy.draw()
    update_canvas()

    handle_events()

    move_toward_obj(boy)
    boy.update()

    delay(0.05)

