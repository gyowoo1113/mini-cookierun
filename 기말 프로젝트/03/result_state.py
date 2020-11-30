import gfw
from pico2d import *
import gobj
from background import Background
import ready_state
from score import Score
from button import Button

def restart():
    gfw.pop()
    gfw.pop()

def add(score):
    global scores
    cw = get_canvas_width()
    ch = get_canvas_height()
    scores = Score(cw/2.5,ch/2,(255,255,250),120)
    scores.score = score
    gfw.world.add(gfw.layer.score,scores)

def build_world():
    gfw.world.init(['bg','score','ui'])
    bg = Background('map_bg/result_bg.png','../res/sound/result.wav','wav')
    gfw.world.add(gfw.layer.bg, bg)

    font =  load_font(gobj.RES_DIR + 'font/CookieRun Regular.ttf',40)

    l,b,w,h = get_canvas_width()/2.5,20,220,90
    btn = Button("",l,b,w,h,font,"ReStart?", lambda: restart())
    gfw.world.add(gfw.layer.ui, btn)

def enter():
    build_world()

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(ready_state)

    # print('ms.he()', e.type, e)
    if handle_mouse(e):
        return

capture = None
def handle_mouse(e):
    global capture
    if capture is not None:
        holding = capture.handle_event(e)
        if not holding:
            capture = None
        return True

    for obj in gfw.world.objects_at(gfw.layer.ui):
        if obj.handle_event(e):
            capture = obj
            return True

    return False

def exit():
    pass

def pause():
    pass

def resume():
    build_world()

if __name__ == '__main__':
    gfw.run_main()