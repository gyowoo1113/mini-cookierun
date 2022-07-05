import gfw
from pico2d import *
import gobj
from background import Background
import ready_state

canvas_width= 1120
canvas_height = 630

def build_world():
    global index,press
    gfw.world.init(['bg',])
    bg = Background('map_bg/title.png','sound/title.wav','wav')
    gfw.world.add(gfw.layer.bg, bg)
    index = 0
    press = False

    global font
    font = load_font(gobj.RES_DIR + 'font/CookieRun Regular.ttf', 20)

def exit():
    pass

def enter():
    build_world()

def update():
    global index,press
    image_count = len(IMAGE_FILES)
    if index < image_count:
        file = IMAGE_FILES[index]
        gfw.image.load(file)
    else:
        press = True
        return
    index += 1

def draw():
    gfw.world.draw()
    if press:
        font.draw(470,200,"press - space bar")

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        if press:
            gfw.push(ready_state)

def exit():
    pass

def pause():
    pass

def resume():
    build_world()

IMAGE_FILES = [
    "res/map_bg/ready_bg.png",
    "res/map_bg/result_bg.png",
    "res/map_bg/bg_1.png",
    "res/map_bg/bg_2.png",
    "res/map_bg/bg_3.png",
    "res/map_bg/choose_bg.png",
    "res/chaser/boss/damage (1).png",
    "res/chaser/boss/damage (2).png",
    "res/chaser/boss/damage (3).png",
    "res/chaser/boss/dead (1).png",
    "res/chaser/boss/dead (2).png",
    "res/chaser/boss/dead (3).png",
    "res/chaser/boss/end (1).png",
    "res/chaser/boss/end (2).png",
    "res/chaser/boss/run (1).png",
    "res/chaser/boss/run (2).png",
    "res/chaser/boss/run (3).png",
    "res/chaser/boss/run (4).png",
    "res/chaser/boss/sleep (1).png",
    "res/chaser/boss/wake (1).png",
    "res/chaser/boss/wake (2).png",
    "res/chaser/boss/wake (3).png",
    "res/chaser/boss/wake (4).png",
    "res/chaser/boss/wake (5).png",
    "res/cookie/cocoa/dead (1).png",
    "res/cookie/cocoa/dead (2).png",
    "res/cookie/cocoa/dead (3).png",
    "res/cookie/cocoa/dead (4).png",
    "res/cookie/cocoa/dead (5).png",
    "res/cookie/cocoa/dead (6).png",
    "res/cookie/cocoa/doublejump (1).png",
    "res/cookie/cocoa/doublejump (2).png",
    "res/cookie/cocoa/doublejump (3).png",
    "res/cookie/cocoa/doublejump (4).png",
    "res/cookie/cocoa/doublejump (5).png",
    "res/cookie/cocoa/doublejump (6).png",
    "res/cookie/cocoa/falling (1).png",
    "res/cookie/cocoa/falling (2).png",
    "res/cookie/cocoa/jump (1).png",
    "res/cookie/cocoa/run (1).png",
    "res/cookie/cocoa/run (2).png",
    "res/cookie/cocoa/run (3).png",
    "res/cookie/cocoa/run (4).png",
    "res/cookie/cocoa/slide (1).png",
    "res/cookie/cocoa/slide (2).png",
    "res/cookie/cocoa/stand (1).png",
    "res/cookie/yogurt/dead (1).png",
    "res/cookie/yogurt/dead (2).png",
    "res/cookie/yogurt/dead (3).png",
    "res/cookie/yogurt/dead (4).png",
    "res/cookie/yogurt/dead (5).png",
    "res/cookie/yogurt/dead (6).png",
    "res/cookie/yogurt/doublejump (1).png",
    "res/cookie/yogurt/doublejump (2).png",
    "res/cookie/yogurt/doublejump (3).png",
    "res/cookie/yogurt/doublejump (4).png",
    "res/cookie/yogurt/doublejump (5).png",
    "res/cookie/yogurt/falling (1).png",
    "res/cookie/yogurt/jump (1).png",
    "res/cookie/yogurt/run (1).png",
    "res/cookie/yogurt/run (2).png",
    "res/cookie/yogurt/run (3).png",
    "res/cookie/yogurt/run (4).png",
    "res/cookie/yogurt/slide (1).png",
    "res/cookie/yogurt/slide (2).png",
    "res/cookie/yogurt/stand (1).png",
    "res/cookie/cocoa.png",
    "res/cookie/yogurt.png",
    "res/cookie/rogue.png",
    "res/cookie/cocoa_pro.png",
    "res/cookie/yogurt_pro.png",
    "res/cookie/rogue_pro.png",
    "res/cookie/rogue/dead (1).png",
    "res/cookie/rogue/dead (2).png",
    "res/cookie/rogue/dead (3).png",
    "res/cookie/rogue/dead (4).png",
    "res/cookie/rogue/dead (5).png",
    "res/cookie/rogue/dead (6).png",
    "res/cookie/rogue/dead (7).png",
    "res/cookie/rogue/dead (8).png",
    "res/cookie/rogue/doublejump (1).png",
    "res/cookie/rogue/doublejump (2).png",
    "res/cookie/rogue/doublejump (3).png",
    "res/cookie/rogue/doublejump (4).png",
    "res/cookie/rogue/doublejump (5).png",
    "res/cookie/rogue/doublejump (6).png",
    "res/cookie/rogue/falling (1).png",
    "res/cookie/rogue/jump (1).png",
    "res/cookie/rogue/jump (2).png",
    "res/cookie/rogue/jump (3).png",
    "res/cookie/rogue/run (1).png",
    "res/cookie/rogue/run (2).png",
    "res/cookie/rogue/run (3).png",
    "res/cookie/rogue/run (4).png",
    "res/cookie/rogue/slide (1).png",
    "res/cookie/rogue/slide (2).png",
    "res/cookie/rogue/stand (1).png",
    "res/jelly/biggest (1).png",
    "res/jelly/biggest (2).png",
    "res/jelly/biggest (3).png",
    "res/jelly/biggest (4).png",
    "res/jelly/bigheart (1).png",
    "res/jelly/bigheart (2).png",
    "res/jelly/bigheart (3).png",
    "res/jelly/bigheart (4).png",
    "res/jelly/bonus (1).png",
    "res/jelly/bonus (2).png",
    "res/jelly/bonus (3).png",
    "res/jelly/bonus (4).png",
    "res/jelly/boss (1).png",
    "res/jelly/heart (1).png",
    "res/jelly/heart (2).png",
    "res/jelly/heart (3).png",
    "res/jelly/heart (4).png",
    "res/jelly/jelly (1).png",
    "res/jelly/magnet (1).png",
    "res/jelly/magnet (2).png",
    "res/jelly/magnet (3).png",
    "res/jelly/magnet (4).png",
    "res/jelly/speed (1).png",
    "res/jelly/speed (2).png",
    "res/jelly/speed (3).png",
    "res/jelly/speed (4).png",
    "res/jelly/start (1).png",
    "res/map_obj/jem (1).png",
    "res/map_obj/jem (2).png",
    "res/map_obj/jem (3).png",
    "res/map_obj/obj05.png",
    "res/map_obj/obj06.png",
    "res/map_obj/obj07.png",
    "res/map_obj/stick_01.png",
    "res/map_obj/stick_02.png",
    "res/map_obj/stick_03.png",
    "res/map_obj/stick_04.png",
    "res/map_obj/straw_01.png",
    "res/map_obj/straw_02.png",
    "res/map_obj/straw_03.png",
    "res/map_obj/straw_04.png",
    "res/map_obj/straw_05.png",
    "res/map_obj/bottom_01.png",
    "res/map_obj/bottom_02.png",
    "res/map_obj/bottom_03.png",
    "res/ui/heart/gauge_bg.png",
    "res/ui/heart/gauge_fg.png",
    "res/ui/heart/heart_icon.png",
    "res/ui/heart/effect.png",
    "res/ui/button/btn_chardown.png",
    "res/ui/button/btn_charnormal.png",
    "res/ui/button/btn_down.png",
    "res/ui/button/btn_normal.png",
    "res/ui/button/btn_xdown.png",
    "res/ui/button/btn_xnormal.png",
]

if __name__ == '__main__':
    gfw.run_main()
