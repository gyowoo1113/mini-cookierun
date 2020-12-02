import gfw
from pico2d import *
import gobj
from background import Background
import main_state
import playerchoose_state
from button import Button,ReadyPlayer

#임시
canvas_width= 1120
canvas_height = 630
cookie_list = ['cocoa','yogurt']

def start():
    for obj in gfw.world.objects_at(gfw.layer.stand):
        main_state.add(obj.char)
    gfw.push(main_state)

def build_world():
    gfw.world.init(['bg','ui','stand'])
    bg = Background('map_bg/ready_bg.png','../res/sound/ready.mp3','mp3')
    gfw.world.add(gfw.layer.bg, bg)

    global frame_interval
    frame_interval = gfw.frame_interval
    gfw.frame_interval = 0

    global name,stand
    name = 'cocoa'
    stand = ReadyPlayer(name,lambda: gfw.push(playerchoose_state))
    gfw.world.add(gfw.layer.stand, stand)

    font = load_font(gobj.RES_DIR + 'font/CookieRun Regular.ttf',40)

    l,b,w,h = get_canvas_width()-220,10,200,90
    btn = Button("",l,b,w,h,font,"Start!!", lambda: start())
    gfw.world.add(gfw.layer.ui, btn)

def change_cookie(n):
    if gfw.world.count_at(gfw.layer.stand) > 0:
        for obj in gfw.world.objects_at(gfw.layer.stand):
            gfw.world.remove(obj)

    stand = ReadyPlayer(n,lambda: gfw.push(playerchoose_state))
    gfw.world.add(gfw.layer.stand, stand)

def enter():
    build_world()

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()
    #gobj.draw_collision_box()

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

    for ui in range(gfw.layer.ui, gfw.layer.stand + 1):
        for obj in gfw.world.objects_at(ui):
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
