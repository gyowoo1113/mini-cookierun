import gfw
from pico2d import *
import gobj
from background import Background
import main_state
from button import Button

#임시
canvas_width= 1120
canvas_height = 630
def start(cookie):
    # player char -> cookie
    gfw.push(main_state)

def build_world():
    gfw.world.init(['bg','ui'])
    bg = Background('map_bg/ready_bg.png','../res/sound/ready.mp3','mp3')
    gfw.world.add(gfw.layer.bg, bg)

    global frame_interval
    frame_interval = gfw.frame_interval
    gfw.frame_interval = 0

    font =  load_font(gobj.RES_DIR + 'font/CookieRun Regular.ttf',40)

    l,b,w,h = get_canvas_width()-220,10,200,90
    btn = Button(l,b,w,h,font,"Start!!", lambda: start("enemy"))
    gfw.world.add(gfw.layer.ui, btn)

def enter():
    build_world()

def update():
    pass

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.pop()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(main_state)

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
    global frame_interval
    gfw.frame_interval = frame_interval

def pause():
    pass

def resume():
    build_world()

if __name__ == '__main__':
    gfw.run_main()
