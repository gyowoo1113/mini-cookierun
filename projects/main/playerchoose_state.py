import gfw
from pico2d import *
import gobj
from background import Background,Pro
import ready_state
from button import Button,ReadyPlayer

#임시
canvas_width= 1120
canvas_height = 630

def change(player):
    gfw.pop()
    ready_state.change_cookie(player)

def build_world():
    gfw.world.init(['bg','ui','pro'])
    bg = Background('map_bg/choose_bg.png','../res/sound/ready.mp3','mp3')
    gfw.world.add(gfw.layer.bg, bg)

    global frame_interval
    frame_interval = gfw.frame_interval
    gfw.frame_interval = 0

#    global name
#    name = 'yogurt'#'cocoa'
#    stand = ReadyPlayer(name,lambda: open(""))
#    gfw.world.add(gfw.layer.ui, stand)

    font =  load_font(gobj.RES_DIR + 'font/CookieRun Regular.ttf',40)

    wh = get_canvas_width()/3 - 60
    l,b,w,h = 70,get_canvas_height()/2-200,wh,wh
    btn = Button("char",l,b,w,h,font,"", lambda: change('cocoa'))
    gfw.world.add(gfw.layer.ui, btn)
    cookie = Pro('cookie/cocoa_pro.png',(l,b,w,h))
    gfw.world.add(gfw.layer.pro, cookie)

    l,b,w,h = 70+wh+20,get_canvas_height()/2-200,wh,wh
    btn = Button("char",l,b,w,h,font,"", lambda: change('yogurt'))
    gfw.world.add(gfw.layer.ui, btn)
    cookie = Pro('cookie/yogurt_pro.png',(l,b,w,h))
    gfw.world.add(gfw.layer.pro, cookie)

    l,b,w,h = 70+wh*2+40,get_canvas_height()/2-200,wh,wh
    btn = Button("char",l,b,w,h,font,"", lambda: change('rogue'))
    gfw.world.add(gfw.layer.ui, btn)
    cookie = Pro('cookie/rogue_pro.png',(l,b,w,h))
    gfw.world.add(gfw.layer.pro, cookie)
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
